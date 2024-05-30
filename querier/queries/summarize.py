# Authors: Thierry Moudiki
#
# License: BSD 3


from .request import request
import pandas as pd
import polars as pl
from ..utils import polars_to_pandas, pandas_to_polars



def summarize(df, req, group_by=None, having=None, **kwargs):
    """ Data summaries on rows.
       
    Args:           
    
        df: a data frame
            a data frame
               
        req: str
            specifying the aggregating operations on columns
           
        group_by: str
                comma-separated list of columns to be aggregated
           
        having: str
               filtering criterion on groups
           
    Examples:
           
        https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
    """

    is_polars = False

    if isinstance(df, pl.DataFrame):
        is_polars = True
        df = polars_to_pandas(df)

    # if request is not None:
    assert group_by is not None, "group_by must be provided"

    ans = "SELECT "
    ans += req
    ans += " FROM df GROUP BY "
    ans += group_by

    if having is not None:
        ans += " HAVING "
        ans += having

    if is_polars:
        return pandas_to_polars(request(df, req=ans, **kwargs))
    return request(df, req=ans, **kwargs)
