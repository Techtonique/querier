# Authors: Thierry Moudiki
#
# License: BSD 3

import pandas as pd
import polars as pl
from ..utils import polars_to_pandas, pandas_to_polars

# creates a copy

def drop(df, req=None):
    """ Drop columns.
       
    Args: 
       
        req: str
            comma-separated list of columns to be dropped
                     
    Examples:     
       
        https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
    """

    try:
        if isinstance(df, pl.DataFrame):
            df = polars_to_pandas(df)

        result = df.drop(req.replace(" ", "").split(","), axis=1)

        if isinstance(df, pl.DataFrame):
            return pandas_to_polars(result)

        return result
    except:
        raise ValueError(
            "request must contain df" "s column names (comma-separated)"
        )
