import numpy as np
import pandas as pd
import unittest as ut
import querier as qr


class Testrequest(ut.TestCase):
    def test_request(self):
        
        df = pd.read_csv("tips.csv")

        df1 = qr.summarize(df, req = "avg(tip), avg(size), sex, time",
                           group_by = "sex, time")
        
        df2 = qr.summarize(df, req ="avg(tip), avg(size), sex, smoker",
                           group_by = "smoker")    
                        
        df['id'] = range(df.shape[0])
        df3 = qr.summarize(df, req = "avg(tip), avg(size), count(id), sex, time",
                           group_by = "sex, time")
        
        self.assertTrue(np.allclose(df1['avg_tip'].values[0], 3.0021153846153843))
        self.assertTrue(np.allclose(df1['avg_tip'].values[1], 2.5828571428571436))
        self.assertTrue(np.allclose(df2['avg_size'].values[0], 2.6688741721854305))
        self.assertTrue(np.allclose(df2['avg_size'].values[1], 2.4086021505376345))
        self.assertTrue(np.allclose(df3['count_id'].values.sum(), df.shape[0]))
