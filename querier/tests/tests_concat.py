import numpy as np
import pandas as pd
import unittest as ut
import querier as qr


class Testconcat(ut.TestCase):
    def test_concat(self):

        np.random.rand(123)
        df1 = pd.DataFrame(
            {"key": ["A", "B", "C", "D"], "value": np.random.randn(4)}
        )
        df2 = pd.DataFrame(
            {"key": ["B", "D", "D", "E"], "value": np.random.randn(4)}
        )
        df3 = pd.DataFrame(
            {"key1": ["A", "B", "C", "D"], "value1": np.random.randn(4)}
        )
        df4 = pd.DataFrame(
            {"key2": ["B", "D", "D", "E"], "value2": np.random.randn(4)}
        )

        df5 = qr.concat(df3, df4, axis="h")
        df6 = qr.concat(df1, df2, axis="v")

        self.assertFalse(
            np.allclose(df5["value1"].values[1], 0.8881945413408756)
        )
        self.assertFalse(np.allclose(df6["value"].values[5], 1.502580905809435))
