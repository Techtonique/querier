"""Delete data"""

# Authors: Thierry Moudiki
#
# License: BSD 3


import numpy as np
from ..utils import parse_request
from ..utils import memoize


# delete(df, 'tip > 1.5')
# delete(df, '(size == 2) | (size == 3)')
@memoize
def delete(df, req=None):

    if req is None:  # useless tho...

        return df

    # if request is not None:
    n, p = df.shape

    str_conds = parse_request(req)

    return df[np.logical_not(eval(str_conds).values)]
