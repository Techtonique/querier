import numpy as np
import pandas as pd
import unittest as ut
import querier as qr


class Testjoin(ut.TestCase):
    def test_join(self):

        np.random.rand(123)
        df1 = pd.DataFrame(
            {
                "key": ["A", "B", "C", "D"],
                "value": np.random.randn(4),
            }
        )
        df2 = pd.DataFrame(
            {
                "key": ["B", "D", "D", "E"],
                "value": np.random.randn(4),
            }
        )

        df3 = qr.join(df1, df2, on="key", type_join="inner")
        df4 = qr.join(df1, df2, on="key", type_join="right")
        df5 = qr.join(df1, df2, on="key", type_join="left")
        df6 = qr.join(df1, df2, on="key", type_join="outer")

        self.assertTrue(
            np.allclose(
                df3["value_x"].values[1], -1.323940985830361
            )
        )
        self.assertTrue(
            np.allclose(
                df4["value_y"].values[1],
                -0.18826506243399763,
            )
        )
        self.assertTrue(
            np.allclose(
                df5["value_x"].values[1],
                -1.7470727330138154,
            )
        )
        self.assertTrue(
            np.allclose(
                df6["value_y"].values[1],
                -0.2597337529898967,
            )
        )
