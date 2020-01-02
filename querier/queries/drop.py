"""Dropping columns"""

# Authors: Thierry Moudiki
#
# License: BSD 3


from ..utils import memoize

# creates a copy
@memoize
def drop(df, req=None):
    try:
        return df.drop(req.replace(" ", "").split(","), axis=1)
    except:
        raise ValueError(
            "request must contain df" "s column names (comma-separated)"
        )
