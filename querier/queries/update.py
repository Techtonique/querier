# Authors: Thierry Moudiki
#
# License: BSD 3


from ..utils import parse_update_request

# modifies input df (!)
# update(df, 'tip = 2*tip')
# update(df, "toto = 3*tip")
# update(df, 'tip = np.mean(tip)')
# update(df, 'toto = np.mean(tip)')
def update(df, req=None):
    """ Update the data frame.
   
    Args:           

        df: a data frame
            a data frame
       
        req: str
            specifying the transformation, e.g `new_size = 3*size`
                 
    Examples: 
   
        https://github.com/thierrymoudiki/querier/tree/master/querier/demo
   
    """

    if req is None:  # useless tho...

        return df

    # if request is not None:
    exec(parse_update_request(req), {"df": df})

    return df
