import numpy as np
import pandas as pd
import unittest as ut
import querier as qr


class Testfiltr(ut.TestCase):
    def test_filtr(self):

        df = pd.read_csv("tips.csv")

        df1 = qr.filtr(df, "tip > 5")
        df2 = qr.filtr(df, "(tip > 5) & (size==2)")
        df3 = qr.filtr(df, "(tip > 5) | (tip < 2)")
        df4 = qr.filtr(df, '(tip > 5) & (sex == "Male")')
        df5 = qr.filtr(df, '(tip > 5) & (sex == "Male") & (smoker == "Yes")')

        self.assertTrue(df1["sex"].values[2] == "Male")
        self.assertTrue(np.allclose(df2["tip"].values[1], 5.15))
        self.assertTrue(df3["day"].values[3] == "Sun")
        self.assertTrue(np.allclose(df4["size"].values[7], 3))
        self.assertTrue(np.allclose(df5["size"].values[4], 4))
