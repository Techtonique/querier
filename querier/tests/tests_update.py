import numpy as np
import pandas as pd
import unittest as ut
import querier as qr
import pandas.util.testing
from pandas.util.testing import assert_frame_equal


class Testupdate(ut.TestCase):
    def test_update(self):
        
        df = pd.read_csv("./tips.csv")
        df1 = qr.update(df, 'tip = 2*tip') # ok
        del df
        
        df = pd.read_csv("./tips.csv")
        df2 = qr.update(df, 'new_tip = 3*tip') # ko 
        del df
        
        df = pd.read_csv("./tips.csv")
        df3 = qr.update(df, 'size = 2+size') # ok  
        del df
        
        df = pd.read_csv("./tips.csv")
        df4 = qr.update(df, 'new_size = 3+size') # ok
        del df
        
        df = pd.read_csv("./tips.csv")
        df5 = qr.update(df, 'tip = tip-1') # ok
        del df
        
        df = pd.read_csv("./tips.csv")
        df6 = qr.update(df, 'new_tip = tip+3') # ok       
        del df
        
        self.assertTrue(np.allclose(df1['tip'].values[2], 7.0))
        self.assertTrue(np.allclose(df2['new_tip'].values[3], 9.93))
        self.assertTrue(np.allclose(df3['size'].values[2], 5))
        self.assertTrue(np.allclose(df4['new_size'].values[3], 5))
        self.assertTrue(np.allclose(df5['tip'].values[3], 2.31))
        self.assertTrue(np.allclose(df6['new_tip'].values[3], 6.31))