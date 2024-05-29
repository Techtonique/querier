# Authors: Thierry Moudiki
#
# License: BSD 3


import numpy as np
from ..utils import parse_request



# delete(df, 'tip > 1.5')
# delete(df, '(size == 2) | (size == 3)')

def delete(df, req=None):
    """Delete rows from a data frame.
       
    Args:           
        
        df: a data frame 
            a data frame
               
        req: str
            criteria for filtering the rows to be deleted
                                 
    Examples:    
           
        https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
    """

    if req is None:  # useless tho...

        return df

    # if request is not None:
    n, p = df.shape

    str_conds = parse_request(req)

    return df[np.logical_not(eval(str_conds).values)]
