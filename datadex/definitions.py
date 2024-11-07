import dagster as dg

import datadex.huggingface.definitions as huggingface_definitions
import datadex.indicators.definitions as indicators_definitions
from datadex.resources import io_manager

common_resources = {"io_manager": io_manager}

definitions = dg.Definitions.merge(
    dg.Definitions(resources=common_resources),
    indicators_definitions.definitions,
    huggingface_definitions.definitions,
)
