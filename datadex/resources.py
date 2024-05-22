import json
import datetime

import httpx
import huggingface_hub as hf_hub
from dagster import InitResourceContext, ConfigurableResource
from datasets import Dataset, NamedSplit
from pydantic import PrivateAttr
from tenacity import retry, wait_exponential, stop_after_attempt


class HuggingFaceResource(ConfigurableResource):
    token: str

    def login(self):
        hf_hub.login(token=self.token)

    def upload_dataset(self, dataset, name):
        self.login()
        dataset = Dataset.from_polars(dataset, split=NamedSplit("main"))
        r = dataset.push_to_hub("datonic/" + name, max_shard_size="50000MB")
        return r


class IUCNRedListAPI(ConfigurableResource):
    token: str

    def get_species(self, page):
        API_ENDPOINT = "https://apiv3.iucnredlist.org/api/v3"

        r = httpx.get(
            f"{API_ENDPOINT}/species/page/{page}?token={self.token}", timeout=30
        )

        r.raise_for_status()

        return r.json()["result"]


class REDataAPI(ConfigurableResource):
    endpoint: str = "https://apidatos.ree.es/en/datos"
    first_day: str = "2014-01-01"

    def query(
        self,
        category: str,
        widget: str,
        start_date: str,
        end_date: str,
        time_trunc: str,
    ):
        params = f"start_date={start_date}T00:00&end_date={end_date}T00:00&time_trunc={time_trunc}"
        url = f"{self.endpoint}/{category}/{widget}?{params}"

        r = httpx.get(url)
        r.raise_for_status()

        return r.json()

    def get_energy_demand(self, start_date: str, end_date: str, time_trunc="hour"):
        category = "demanda"
        widget = "demanda-tiempo-real"
        return self.query(category, widget, start_date, end_date, time_trunc)

    def get_market_prices(self, start_date: str, end_date: str, time_trunc="hour"):
        category = "mercados"
        widget = "precios-mercados-tiempo-real"
        return self.query(category, widget, start_date, end_date, time_trunc)


class AEMETAPI(ConfigurableResource):
    endpoint: str = "https://opendata.aemet.es/opendata/api"
    token: str

    _client: httpx.Client = PrivateAttr()

    def setup_for_execution(self, context: InitResourceContext) -> None:
        transport = httpx.HTTPTransport(retries=5)
        limits = httpx.Limits(max_keepalive_connections=2, max_connections=2)
        self._client = httpx.Client(
            transport=transport,
            limits=limits,
            http2=True,
            base_url=self.endpoint,
            timeout=60,
        )

    @retry(
        stop=stop_after_attempt(10),
        wait=wait_exponential(min=1, max=30),
    )
    def query(self, url):
        headers = {"cache-control": "no-cache"}

        query = {
            "api_key": self.token,
        }

        response = self._client.get(url, headers=headers, params=query)
        response.raise_for_status()

        data_url = response.json().get("datos")
        if data_url is None:
            raise ValueError(f"The 'datos' field is not correct. {response.json()}")

        r = self._client.get(data_url, timeout=30)
        r.raise_for_status()

        data = json.loads(r.text.encode("utf-8"))

        return data

    def get_weather_data(
        self, start_date: datetime.datetime, end_date: datetime.datetime
    ):
        start_date_str = start_date.strftime("%Y-%m-01") + "T00:00:00UTC"
        end_date_str = end_date.strftime("%Y-%m-01") + "T00:00:00UTC"

        current_date = start_date
        all_data = []

        while current_date < end_date:
            next_date = min(current_date + datetime.timedelta(days=31), end_date)

            start_date_str = current_date.strftime("%Y-%m-%d") + "T00:00:00UTC"
            end_date_str = next_date.strftime("%Y-%m-%d") + "T00:00:00UTC"

            url = f"/valores/climatologicos/diarios/datos/fechaini/{start_date_str}/fechafin/{end_date_str}/todasestaciones"
            data = self.query(url)

            all_data.extend(data)

            current_date = next_date + datetime.timedelta(days=1)

        return all_data

    def get_all_stations(self):
        url = "/valores/climatologicos/inventarioestaciones/todasestaciones"

        return self.query(url)

    def teardown_after_execution(self, context: InitResourceContext) -> None:
        self._client.close()


class MITECOArcGisAPI(ConfigurableResource):
    endpoint: str = (
        "https://services-eu1.arcgis.com/RvnYk1PBUJ9rrAuT/ArcGIS/rest/services/"
    )

    @retry(
        stop=stop_after_attempt(10),
        wait=wait_exponential(multiplier=1, min=4, max=20),
    )
    def query(self, dataset_name, params=None):
        url = f"{self.endpoint}/{dataset_name}/FeatureServer/0/query"
        default_params = {"resultType": "standard", "outFields": "*", "f": "pjson"}
        query_params = {**default_params, **params} if params else default_params

        r = httpx.get(url, params=query_params)
        r.raise_for_status()

        return r.json()

    def get_water_reservoirs_data(self, start_date=None, end_date=None):
        if start_date and end_date:
            date_format = "%Y-%m-%d"
            params = {
                "where": f"fecha BETWEEN timestamp '{start_date.strftime(date_format)}' "
                f"AND timestamp '{end_date.strftime(date_format)}'"
            }
        else:
            params = None
        query_response = self.query(dataset_name="Embalses_Total", params=params)

        return query_response
