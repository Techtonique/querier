"""Select data"""

# Authors: Thierry Moudiki
#
# License: BSD 3


import numpy as np
from ..utils import memoize


# select(df, req='tip, sex', limit=4, random=True, seed=5)
# select(df, req='tip, sex, smoker', limit=4, random=True, seed=7)
# select(df, req='tip, sex, day', limit=3, random=False, seed=10)
# select(df, req='*', limit=7, random=False, seed=10)
# select(df, req='*', limit=7, random=True, seed=1430)
# select(df, req="day, time, sex", limit=10, random=True, seed=140)
# select(df, req="day, time, sex")
@memoize
def select(df, req="*", order_by=None, asc=True, 
           limit=None, random=False, seed=123):

    n, p = df.shape
    
    if order_by is not None:
        order_by_ = order_by.replace(" ", "").split(',')

    if req == "*":

        if limit is not None:

            assert (
                int(limit) == limit
            ), "limit must be an integer"

            if random == False:

                return df.head(limit)

            # if random == True:
            np.random.seed(seed)
            return df.iloc[
                np.random.randint(
                    low=0, high=n, size=limit
                ),
            ]

        # if limit is not None:
        if order_by is None:
            
            return df
        
        return df.sort_values(by=order_by_, ascending=asc)

    # if col_names != "*":
    str_col_names = req.replace(" ", "")
    str_col_names = "'" + str_col_names + "'"
    str_col_names = str_col_names.replace(",", "', '")

    if limit is not None:

        assert (
            int(limit) == limit
        ), "limit must be an integer"

        if random == False:
            
            if order_by is None:
            
                try:
                    return eval(
                        "df[["
                        + str_col_names
                        + "]].head(limit)"
                    )
                except:
                    raise ValueError(
                        "request must contain df"
                        "s column names (comma-separated)"
                    )

        # if random == True:
        if order_by is None:
        
            try:
                return eval(
                    "df[["
                    + str_col_names
                    + "]].iloc[np.random.randint(low=0, high=n, size=limit),:]"
                )
            except:
                raise ValueError(
                    "request must contain df"
                    "s column names (comma-separated)"
                )
        
        # if order_by is not None:
        try:
            return eval(
                "df[["
                + str_col_names
                + "]].iloc[np.random.randint(low=0, high=n, size=limit),:].sort_values(by=order_by_, ascending=asc)"
            )
        except:
            raise ValueError(
                "request must contain df"
                "s column names (comma-separated)"
            )

    # if limit is None:
    if order_by is None:
        
        try:
            return eval("df[[" + str_col_names + "]]")
        except:
            raise ValueError(
                "request must contain df"
                "s column names (comma-separated)"
            )
            
    # if order_by is not None:
    try:
        return eval("df[[" + str_col_names + "]].sort_values(by=order_by_, ascending=asc)")
    except:
        raise ValueError(
                "request must contain df"
                "s column names (comma-separated)"
            )