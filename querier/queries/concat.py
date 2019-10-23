"""Concatenate data frames"""

# Authors: Thierry Moudiki
#
# License: BSD 3


import pandas as pd
import numpy as np


# df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
#                     'value': np.random.randn(4)})
# df2 = pd.DataFrame({'key': ['B', 'D', 'D', 'E'],
#                    'value': np.random.randn(4)})
# print(concat(df1, df2, axis="h"))
def concat(df1, df2, axis="h", **kwargs):

    assert axis in (
        "h",
        "v",
    ), "must have axis in ('h', 'v')"

    if axis == "h":

        assert (
            len(
                np.intersect1d(
                    df1.columns.values,
                    np.array(["key2", "value2"]),
                )
            )
            == 0
        ), "df1 and df2 must have different column names (try function join instead)"

        df = pd.DataFrame(np.hstack((df1, df2)))

        df.columns = np.append(
            df1.columns.values, df2.columns.values
        )

        return df

    # if axis == "v":
    assert (
        df1.columns.values == df2.columns.values
    ).all(), "must have: df1.columns == df2.columns"

    df = pd.DataFrame(np.vstack((df1, df2)))

    df.columns = df1.columns.values

    return df.drop_duplicates()
