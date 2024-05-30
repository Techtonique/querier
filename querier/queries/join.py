# Authors: Thierry Moudiki
#
# License: BSD 3


import pandas as pd
import polars as pl
from ..utils import polars_to_pandas, pandas_to_polars

# just for 'completeness' of the interface
# already straightforward in pd

# df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
#                     'value': np.random.randn(4)})
# df2 = pd.DataFrame({'key': ['B', 'D', 'D', 'E'],
#                    'value': np.random.randn(4)})
# join(df1, df2, on='key')
# join(df1, df2, 'key', "left")
# join(df1, df2, 'key', "right")
# join(df1, df2, 'key', "outer")

def join(df1, df2, on=None, type_join="inner", **kwargs):
    """ Join data frames.
   
    Args:
    
        df1: a data frame           
           a data frame
       
        df2: a data frame           
           a data frame
       
        on: str
           joining column/criterion
       
        type_join: str           
           type of join. Options are: "left", "right", "outer", "inner". 
           Default is "inner" join.              
       
    Examples: 
       
        https://github.com/thierrymoudiki/querier/tree/master/querier/demo
   
   """
    if on is not None:
        on_ = on.replace(" ", "").split(",")

    if isinstance(df1, pl.DataFrame):
         df1 = polars_to_pandas(df1)
         df2 = polars_to_pandas(df2)

    result = pd.merge(df1, df2, on=on_, how=type_join, **kwargs)

    if isinstance(df1, pl.DataFrame):
        return pandas_to_polars(result)
    
    return result
