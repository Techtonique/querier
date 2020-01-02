"""Join data frames"""

# Authors: Thierry Moudiki
#
# License: BSD 3


import pandas as pd
from ..utils import memoize


# just for 'completeness' of the interface
# already straightforward in pd

# df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
#                     'value': np.random.randn(4)})
# df2 = pd.DataFrame({'key': ['B', 'D', 'D', 'E'],
#                    'value': np.random.randn(4)})
# join(df1, df2, on='key')
# join(df1, df2, 'key', "left")
# join(df1, df2, 'key', "right")
# join(df1, df2, 'key', "outer")
@memoize
def join(df1, df2, on=None, type_join="inner", **kwargs):

    if on is not None:
        on_ = on.replace(" ", "").split(",")

    return pd.merge(df1, df2, on=on_, how=type_join, **kwargs)
