import numpy as np
import pandas as pd
import unittest as ut
import querier as qr


class Testdelete(ut.TestCase):
    def test_delete(self):
        
        df = pd.read_csv("tips.csv")

        df1 = qr.delete(df, 'tip > 5')        
        df2 = qr.delete(df, '(tip > 5) & (size==2)')        
        df3 = qr.delete(df, '(tip > 5) | (tip < 2)')        
        df4 = qr.delete(df, '(tip > 5) & (sex == "Male")')        
        df5 = qr.delete(df, '(tip > 5) & (sex == "Male") & (smoker == "Yes")')        
        
        self.assertTrue(df1.shape[0] == 226)
        self.assertTrue(np.allclose(df1['tip'].values.mean(), 
                                    2.7374336283185836))
        self.assertTrue(df2.shape[0] == 241)
        self.assertTrue(np.allclose(df2['tip'].values.mean(), 
                                    2.9665145228215772))
        self.assertTrue(df3.shape[0] == 181)
        self.assertTrue(np.allclose(df3['tip'].values.mean(), 
                                    3.0450828729281767))
        self.assertTrue(df4.shape[0] == 230)
        self.assertTrue(np.allclose(df4['tip'].values.mean(), 
                                    2.785521739130435))
        self.assertTrue(df5.shape[0] == 239)
        self.assertTrue(np.allclose(df5['tip'].values.mean(), 
                                    2.9251882845188284))
