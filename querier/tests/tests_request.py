import numpy as np
import pandas as pd
import unittest as ut
import querier as qr


class Testrequest(ut.TestCase):
    def test_request(self):

        df = pd.read_csv("tips.csv")

        df1 = qr.request(
            df,
            "SELECT tip, smoker, day FROM df WHERE tip > 2",
        )
        df2 = qr.request(
            df,
            "SELECT tip, smoker, day, size FROM df WHERE (tip > 2) and (size > 4)",
        )
        df3 = qr.request(
            df,
            "SELECT tip, smoker, day, size FROM df WHERE (tip > 2) and (size > 4) and (day not like 'Thur')",
        )
        df4 = qr.request(
            df,
            "SELECT AVG(tip) as avg_tip, size, smoker FROM df WHERE tip > 2 GROUP BY size",
        )
        df5 = qr.request(
            df,
            "SELECT avg(tip) as avg_tip, AVG(size) as   avg_size, smoker FROM df WHERE tip > 2 GROUP BY size, tip",
        )

        self.assertTrue(df1.shape[0] == 166)
        self.assertTrue(np.min(df1["tip"].values) == 2.01)
        self.assertTrue(df2.shape[0] == 8)
        self.assertTrue(np.min(df2["size"].values) == 5)
        self.assertTrue(df3.shape[0] == 4)
        self.assertTrue(np.min(df3["size"].values) == 5)
        self.assertTrue(df4.shape[0] == 5)
        self.assertTrue(
            np.min(df4["avg_tip"].values)
            == 3.180430107526883
        )
        self.assertTrue(df5.shape[0] == 110)
        self.assertTrue(
            np.min(df5["avg_tip"].values) == 2.01
        )
