"""Update data"""

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

    if req is None:  # useless tho...

        return df

    # if request is not None:
    exec(parse_update_request(req), {"df": df})

    return df
