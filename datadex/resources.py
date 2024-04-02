import requests
import huggingface_hub as hf_hub
from dagster import ConfigurableResource
from datasets import Dataset, NamedSplit
from tenacity import retry, wait_exponential, stop_after_attempt


class HuggingFaceResource(ConfigurableResource):
    token: str

    def login(self):
        hf_hub.login(token=self.token)

    def upload_dataset(self, dataset, name):
        self.login()
        dataset = Dataset.from_pandas(dataset, split=NamedSplit("main"))
        r = dataset.push_to_hub(
            "davidgasquez/" + name, max_shard_size="50000MB"
        )
        return r


class IUCNRedListAPI(ConfigurableResource):
    token: str

    def get_species(self, page):
        API_ENDPOINT = "https://apiv3.iucnredlist.org/api/v3"
        r = requests.get(f"{API_ENDPOINT}/species/page/{page}?token={self.token}")
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
        r = requests.get(url)
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

    @retry(
        stop=stop_after_attempt(10),
        wait=wait_exponential(multiplier=1, min=4, max=20),
    )
    def query(self, url):
        query = {
            "api_key": self.token,
        }

        headers = {"cache-control": "no-cache"}
        r = requests.get(url, params=query, headers=headers)
        r.raise_for_status()

        return r.json()

    @retry(
        stop=stop_after_attempt(10),
        wait=wait_exponential(multiplier=1, min=4, max=20),
    )
    def get_query_data(self, query_response):
        data_url = query_response.get("datos")
        r = requests.get(data_url)
        r.raise_for_status()

        return r.json()

    def get_all_stations(self):
        url = f"{self.endpoint}/valores/climatologicos/inventarioestaciones/todasestaciones"

        query_response = self.query(url)
        data = self.get_query_data(query_response)

        return data

    def get_weather_data(self, start_date: str, end_date: str):
        url = f"{self.endpoint}/valores/climatologicos/diarios/datos/fechaini/{start_date}/fechafin/{end_date}/todasestaciones"

        query_response = self.query(url)
        data = self.get_query_data(query_response)

        return data
