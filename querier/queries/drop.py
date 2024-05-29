# Authors: Thierry Moudiki
#
# License: BSD 3




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
        return df.drop(req.replace(" ", "").split(","), axis=1)
    except:
        raise ValueError(
            "request must contain df" "s column names (comma-separated)"
        )
