import numpy as np
import pandas as pd
import unittest as ut
import querier as qr


class Testselect(ut.TestCase):
    def test_select(self):

        df = pd.read_csv("tips.csv")

        df1 = qr.select(df, "tip, sex, smoker")
        df2 = qr.select(df, "tip, day, time", limit=5)
        df3 = qr.select(df, "smoker, day, total_bill", limit=5, random=True)
        df4 = qr.select(df, "*", limit=5)
        df5 = qr.select(df, "*", limit=5, random=True)

        self.assertTrue(df1["sex"].values[2] == "Male")
        self.assertTrue(np.allclose(df2["tip"].values[1], 1.66))
        self.assertTrue(df3["day"].values[3] == "Sat")
        self.assertTrue(np.allclose(df4["tip"].values[3], 3.31))
        self.assertTrue(np.allclose(df5["total_bill"].values[0], 14.31))
