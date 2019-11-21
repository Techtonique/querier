"""Wrapper for the querier's operations."""

# Authors: Thierry Moudiki
#
# License: BSD 3


import pandas as pd
from sklearn.base import BaseEstimator
from ..queries import select as select_, update as update_, delete as delete_,\
 concat as concat_, filtr as filtr_, join as join_, summarize as summarize_,\
 drop as drop_, request as request_


class Querier(BaseEstimator):
    """Wrapper for the querier's operations.
       
       Parameters
       ----------
       df: a data frame
           a data frame    
    """
        
    def __init__(self, df):    
        assert isinstance(df, pd.DataFrame),\
        "attribute 'df' must be a data frame"
        
        self.df = df
    
    def select(self, req='*', order_by=None, asc=True, limit=None, 
               random=False, seed=123):
        self.df = select_(self.df, req, order_by, asc, limit, random, seed)
        return self
    
    def update(self, req=None):
        self.df = update_(self.df, req)
        return self    

    def delete(self, req=None):
        self.df = delete_(self.df, req)
        return self
    
    def concat(self, df2, axis='h', **kwargs):
        assert isinstance(df2, pd.DataFrame),\
        "'df2' must be a data frame"
        self.df = concat_(self.df, df2, axis, **kwargs)
        return self
    
    def filtr(self, req=None, limit=None, random=False, seed=123):
        self.df = filtr_(self.df, req, limit, random, seed)
        return self
    
    def join(self, df2, on=None, type_join='inner', **kwargs):
        assert isinstance(df2, pd.DataFrame),\
        "'df2' must be a data frame"
        self.df = join_(self.df, df2, on, type_join, **kwargs)
        return self
    
    def summarize(self, req=None, group_by=None, having=None, **kwargs):
        self.df = summarize_(self.df, req, group_by, having, **kwargs)
        return self
    
    def drop(self, req=None):
        self.df = drop_(self.df, req)
        return self
    
    def request(self, req=None, **kwargs):
        self.df = request_(self.df, req, **kwargs)
        return self
    