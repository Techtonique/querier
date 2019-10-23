import numpy as np
import pandas as pd
import unittest as ut
import querier as qr


class Testdrop(ut.TestCase):
    def test_drop(self):

        df = pd.read_csv("tips.csv")

        df1 = qr.drop(df, "total_bill")
        df2 = qr.drop(df, "tip")
        df3 = qr.drop(df, "sex")
        df4 = qr.drop(df, "smoker")
        df5 = qr.drop(df, "day")
        df6 = qr.drop(df, "total_bill, tip, sex, day")

        self.assertTrue(df1.shape[1] == 6)
        self.assertTrue(
            "total_bill" not in df1.columns.values
        )
        self.assertTrue(df2.shape[1] == 6)
        self.assertTrue("tip" not in df2.columns.values)
        self.assertTrue(df3.shape[1] == 6)
        self.assertTrue("sex" not in df3.columns.values)
        self.assertTrue(df4.shape[1] == 6)
        self.assertTrue("smoker" not in df4.columns.values)
        self.assertTrue(df5.shape[1] == 6)
        self.assertTrue("day" not in df5.columns.values)
        self.assertTrue(
            df6.columns.values
            == np.array(
                ["smoker", "time", "size"], dtype=object
            ).all()
        )
