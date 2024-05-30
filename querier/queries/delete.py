# Authors: Thierry Moudiki
#
# License: BSD 3


import numpy as np
import polars as pl
from ..utils import parse_request
from ..utils import polars_to_pandas, pandas_to_polars


# delete(df, 'tip > 1.5')
# delete(df, '(size == 2) | (size == 3)')

def delete(df, req):
    """Delete rows from a data frame.
       
    Args:           
        
        df: a data frame 
            a data frame
               
        req: str
            criteria for filtering the rows to be deleted
                                 
    Examples:    
           
        https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
    """

    if isinstance(df, pl.DataFrame):
            
        df = polars_to_pandas(df)

    # if request is not None:
    n, p = df.shape

    str_conds = parse_request(req)

    result = df[np.logical_not(eval(str_conds).values)]

    if isinstance(df, pl.DataFrame):

        return pandas_to_polars(result)

    return result 
