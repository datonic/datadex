from dagster.components import definitions, load_defs

import datadex.defs


@definitions
def defs():
    return load_defs(defs_root=datadex.defs)
