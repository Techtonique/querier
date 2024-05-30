# Authors: Thierry Moudiki
#
# License: BSD 3

import pandas as pd
import polars as pl
from ..utils import parse_update_request
from ..utils import polars_to_pandas, pandas_to_polars

# modifies input df (!)
# update(df, 'tip = 2*tip')
# update(df, "toto = 3*tip")
# update(df, 'tip = np.mean(tip)')
# update(df, 'toto = np.mean(tip)')
def update(df, req):
    """ Update the data frame.
   
    Args:           

        df: a data frame
            a data frame
       
        req: str
            specifying the transformation, e.g `new_size = 3*size`
                 
    Examples: 
   
        https://github.com/thierrymoudiki/querier/tree/master/querier/demo
   
    """
    
    is_polars = False

    if isinstance(df, pl.DataFrame):
        is_polars = True
        df = polars_to_pandas(df)

    # if request is not None:
    exec(parse_update_request(req), {"df": df})

    if is_polars:
        return pandas_to_polars(df)
    return df
