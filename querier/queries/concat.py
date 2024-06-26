# Authors: Thierry Moudiki
#
# License: BSD 3


import pandas as pd
import polars as pl
import numpy as np
from ..utils import polars_to_pandas, pandas_to_polars



# df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
#                     'value': np.random.randn(4)})
# df2 = pd.DataFrame({'key': ['B', 'D', 'D', 'E'],
#                    'value': np.random.randn(4)})
# print(concat(df1, df2, axis="h"))

def concat(df1, df2, axis="h", **kwargs):
    """Concatenate data frames.
       
    Args:           
        
        df1: a data frame
            a data frame
           
        df2: a data frame           
            a data frame
           
        axis: str
            specify the type of concatenation: "h"=horizontal, "v"=vertical
                                 
    Examples:
           
        https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
    """

    assert axis in ("h", "v"), "must have axis in ('h', 'v')"

    if isinstance(df1, pl.DataFrame):
        df1 = polars_to_pandas(df1)
    
    if isinstance(df2, pl.DataFrame):
        df2 = polars_to_pandas(df2)

    if axis == "h":

        assert (
            len(
                np.intersect1d(df1.columns.values, np.array(["key2", "value2"]))
            )
            == 0
        ), "df1 and df2 must have different column names (try function join instead)"

        df = pd.DataFrame(np.hstack((df1, df2)))

        df.columns = np.append(df1.columns.values, df2.columns.values)

        if isinstance(df1, pl.DataFrame):
            return polars_to_pandas(df)
        return df

    # if axis == "v":
    assert (
        df1.columns.values == df2.columns.values
    ).all(), "must have: df1.columns == df2.columns"

    df = pd.DataFrame(np.vstack((df1, df2)))

    df.columns = df1.columns.values

    if isinstance(df1, pl.DataFrame):
        return polars_to_pandas(df)
    return df.drop_duplicates()
