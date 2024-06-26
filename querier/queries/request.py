# Authors: Thierry Moudiki
#
# License: BSD 3


import pandas as pd
import polars as pl
from sqlalchemy import create_engine, text 
from ..utils import parse_cols_request
from ..utils import polars_to_pandas, pandas_to_polars


# request(df, "SELECT tip, smoker, day FROM df WHERE tip > 25")
# request(df, "SELECT tip, smoker, day, size FROM df WHERE (tip > 2) and (size > 4)")
# request(df, "SELECT tip, smoker, day, size FROM df WHERE (tip > 2) and (size > 4) and (day like 'Thur')")
# request(df, "SELECT tip, smoker, day, size FROM df WHERE (tip > 2) and (size > 4) and (day not like 'Thur')")
# request(df, "SELECT SUM(tip), smoker FROM df WHERE tip > 20 GROUP BY smoker")
# request(df, "SELECT AVG(tip), size, smoker FROM df WHERE tip > 20 GROUP BY size")
# request(df, "SELECT AVG(tip) as avg_tip, size, smoker FROM df WHERE tip > 20 GROUP BY size")
# request(df, "SELECT avg(tip) as avg_tip, AVG(size) as   avg_size, smoker FROM df WHERE tip > 20 GROUP BY size, tip")
# request(df, "SELECT SUM(tip), smoker FROM df GROUP BY smoker having tip > 1.5")

def request(df, req, **kwargs):
    """ SQL request on a data frame.
       
    Args:           
    
        df: a data frame
            a data frame
           
        req: str
            specifying the SQL request
                      
           
    Examples:           
           
        https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
    """

    # if req is not None:
    assert (
        "UPDATE".lower() not in req.lower()
    ), "'UPDATE' is forbidden here, try querier.update"

    assert (
        "DELETE".lower() not in req.lower()
    ), "'DELETE' is forbidden here, try querier.delete"

    assert (
        "DROP".lower() not in req.lower()
    ), "'DROP' is forbidden here, try querier.drop"

    try:

        engine = create_engine("sqlite://", echo=False)
        df.to_sql("df", con=engine, **kwargs)
        with engine.connect() as conn:
            req_res = conn.execute(text(req.upper())).fetchall()
        col_names = parse_cols_request(req)
        result = pd.DataFrame(req_res, columns=col_names)
        if isinstance(df, pl.DataFrame):
            return(pandas_to_polars(result))
        return result

    except:

        raise ValueError("invalid request: check SQL syntax")
