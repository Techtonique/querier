# Authors: Thierry Moudiki
#
# License: BSD 3


import numpy as np
import pandas as pd
import polars as pl
from ..utils import parse_request
from ..utils import polars_to_pandas, pandas_to_polars



# filtr(df, 'tip > 5')
# req = "(time == 'Dinner') & (day == 'Sun') & (tip>1.5)"
# filtr(df, req, limit=3, random=False)
# filtr(df, req, limit=4, random=True)
#
# req = "(tip>1.5)"
# filtr(df, req, limit=7, random=False)œ
# filtr(df, req, limit=5, random=True)
#
# req = "(tip > 5) & (size > 3)"
# filtr(df, req, limit=5, random=False)
# filtr(df, req, limit=8, random=True)
#
# req = "(tip > 5) & (size > 3) & (sex == 'Male')"
# filtr(df, req, limit=7, random=False)
# filtr(df, req, limit=8, random=True)

def filtr(df, req, limit=None, random=False, seed=123):
    """ Filter rows, based on given criteria.
   
    Args:    

        req: str
            criteria for filtering the rows

        limit: int
            number of records to be retrieved 
        
        random: bool
            `True` if we want a random set of records 
           
        seed: int
            reproducibility seed for situations where `random == True`
                     
    Examples:           
       
        https://github.com/thierrymoudiki/querier/tree/master/querier/demo
   
    """

    if isinstance(df, pl.DataFrame):

        df = polars_to_pandas(df)

    # if request is not None:
    n, p = df.shape

    str_conds = parse_request(req)

    df_res = df[eval(str_conds)]

    if limit is not None:

        assert int(limit) == limit, "limit must be an integer"

        if random == False:

            try:
                if isinstance(df, pl.DataFrame):
                    return pandas_to_polars(df_res.head(limit))
                return df_res.head(limit)
            except:
                raise ValueError(
                    "invalid request: check column names + contents (and parentheses for multiple conditions)"
                )

        # if random == True:
        try:
            np.random.seed(seed)
            df_res.iloc[
                np.random.choice(
                    range(0, df_res.shape[0]), size=limit, replace=False
                ),
            ]
            if isinstance(df, pl.DataFrame):
                return pandas_to_polars(df_res)
            return df_res
        except:
            raise ValueError(
                "invalid request: check column names + contents (and parentheses for multiple conditions)"
            )

    # if limit is None:
    try:
        if isinstance(df, pl.DataFrame):
            return pandas_to_polars(df_res)
        return df_res
    except:
        raise ValueError(
            "invalid request: check column names + contents (and parentheses for multiple conditions)"
        )
