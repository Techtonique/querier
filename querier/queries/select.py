# Authors: Thierry Moudiki
#
# License: BSD 3


import numpy as np
import pandas as pd
import polars as pl
from ..utils import polars_to_pandas, pandas_to_polars



# select(df, req='tip, sex', limit=4, random=True, seed=5)
# select(df, req='tip, sex, smoker', limit=4, random=True, seed=7)
# select(df, req='tip, sex, day', limit=3, random=False, seed=10)
# select(df, req='*', limit=7, random=False, seed=10)
# select(df, req='*', limit=7, random=True, seed=1430)
# select(df, req="day, time, sex", limit=10, random=True, seed=140)
# select(df, req="day, time, sex")

def select(
    df, req="*", order_by=None, asc=True, limit=None, random=False, seed=123
):
    """ Select columns.
       
    Args:

        df: a data frame
            a data frame
        
        req: str
            comma-separated columns names
        
        order_by: str
            sort the results by using these columns (optional)
        
        asc: bool
            if `order_by` is provided, `True` means: ascending ordering 
        
        limit: int
            number of records to be retrieved 

        random: bool
            `True` if we want a random set of records 
        
        seed: int
            reproducibility seed for situations where `random == True`
       
    Examples: 
       
       https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
    """
    
    is_polars = False

    if isinstance(df, pl.DataFrame):
        is_polars = True
        df = polars_to_pandas(df)

    n, p = df.shape

    if order_by is not None:
        order_by_ = order_by.replace(" ", "").split(",")

    if req == "*":

        if limit is not None:

            assert int(limit) == limit, "limit must be an integer"

            if random == False:  
                if is_polars:
                    return pandas_to_polars(df.head(limit))                              
                return df.head(limit)

            # if random == True:
            np.random.seed(seed)
            result = df.iloc[np.random.randint(low=0, high=n, size=limit),]
            if is_polars:
                return pandas_to_polars(result)
            return result

        # if limit is not None:
        if order_by is None:
            if is_polars:
                return pandas_to_polars(df)
            return df

        if is_polars:
            return pandas_to_polars(df.sort_values(by=order_by_, ascending=asc))
        return df.sort_values(by=order_by_, ascending=asc)

    # if col_names != "*":
    str_col_names = req.replace(" ", "")
    str_col_names = "'" + str_col_names + "'"
    str_col_names = str_col_names.replace(",", "', '")

    if limit is not None:

        assert int(limit) == limit, "limit must be an integer"

        if random == False:

            if order_by is None:

                try:
                    result = eval("df[[" + str_col_names + "]].head(limit)")
                    if is_polars:
                        return pandas_to_polars(result) 
                    return result
                except:
                    raise ValueError(
                        "request must contain df"
                        "s column names (comma-separated)"
                    )

        # if random == True:
        if order_by is None:

            try:
                result = eval(
                    "df[["
                    + str_col_names
                    + "]].iloc[np.random.randint(low=0, high=n, size=limit),:]"
                )
                if is_polars:
                    return pandas_to_polars(result) 
                return result
            except:
                raise ValueError(
                    "request must contain df" "s column names (comma-separated)"
                )

        # if order_by is not None:
        try:
            result = eval(
                "df[["
                + str_col_names
                + "]].iloc[np.random.randint(low=0, high=n, size=limit),:].sort_values(by=order_by_, ascending=asc)"
            )
            if is_polars:
                return pandas_to_polars(result)
            return result
        except:
            raise ValueError(
                "request must contain df" "s column names (comma-separated)"
            )

    # if limit is None:
    if order_by is None:

        try:
            result = eval("df[[" + str_col_names + "]]")
            if is_polars:
                return pandas_to_polars(result)
            return result
        except:
            raise ValueError(
                "request must contain df" "s column names (comma-separated)"
            )

    # if order_by is not None:
    try:
        result = eval(
            "df[["
            + str_col_names
            + "]].sort_values(by=order_by_, ascending=asc)"
        )
        if is_polars:
            return pandas_to_polars(result)
        return result
    except:
        raise ValueError(
            "request must contain df" "s column names (comma-separated)"
        )
