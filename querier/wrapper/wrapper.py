"""Wrapper for the querier's operations."""

# Authors: Thierry Moudiki
#
# License: BSD 3


import pandas as pd
from sklearn.base import BaseEstimator
import sqlite3
from pymongo import MongoClient

from ..queries import (
    select as select_,
    update as update_,
    delete as delete_,
    concat as concat_,
    filtr as filtr_,
    join as join_,
    summarize as summarize_,
    drop as drop_,
    request as request_,
)


class Querier(BaseEstimator):
    """Wrapper for the querier's operations.
       
       Parameters
       ----------
       df: a data frame
           a data frame (optional)
           
       source: str
           a csv file path, sql database path, or mongo db uri
                 
       db: str
           database name, if `source` is a mongo db uri
                 
       table: str
           name of the table/collection, if `source` is provided
    """

    def __init__(self, 
                 df=None, 
                 source=None,
                 db=None,
                 table=None,
                 **kwargs):

        
        if (df is not None) & isinstance(df, pd.DataFrame): 
            
            assert (source is None) & (table is None),\
            "No `source` required when `df` is provided"
            
            self.df = df

            
        elif (source is not None):   
            
            assert (df is None),\
            "`df` is no used when `source` is provided"
            
            self.source = source
                        
            if self.source[-3:] == 'csv': 
                
                self.df = pd.read_csv(self.source, 
                                      **kwargs)
            
            elif self.source[0:7] == 'mongodb': 
                
                assert (table is not None) & (isinstance(table, str)),\
                "`table` name must be (a string) provided along with database `source`"
                
                assert (db is not None) & (isinstance(db, str)),\
                "A database `db` must be provided"
                
                self.table = table
                self.conn = MongoClient(self.source, **kwargs)   
                self.db = self.conn[db]
                self.df = pd.DataFrame(list(self.db[table].find()))
                
            else: # other db source 
                
                assert (table is not None) & (isinstance(table, str)),\
                "`table` name must be (a string) provided along with db `source`"
                
                self.table = table
                
                try:
                                        
                    self.df = pd.read_sql_table(table_name=self.table, 
                                                con=self.source, 
                                                **kwargs)
                    
                except:
                    
                    try: # sqlite3 source
                    
                        self.conn = sqlite3.connect(self.source, 
                                                    **kwargs)                    
                        self.df = pd.read_sql_query("SELECT * FROM " + self.table, 
                                                    con=self.conn, 
                                                    **kwargs)
                    
                    except: 
                        
                        raise ValueError("Database format not supported")                                          
                                                
        else:  
            
            raise ValueError("Check database format provided in `source`")                                          
            
           
        self.colnames = self.df.columns.values
        self.rownames = self.df.index.values
        self.nrows = self.df.shape[0]
        self.ncols = self.df.shape[1]
        self.dtypes = self.df.dtypes.values

    def select(
        self,
        req="*",
        order_by=None,
        asc=True,
        limit=None,
        random=False,
        seed=123,
    ):
        self.df = select_(self.df, req, order_by, asc, limit, random, seed)
        return self

    def update(self, req=None):
        self.df = update_(self.df, req)
        return self

    def delete(self, req=None):
        self.df = delete_(self.df, req)
        return self

    def concat(self, df2, axis="h", **kwargs):
        assert isinstance(df2, pd.DataFrame), "'df2' must be a data frame"
        self.df = concat_(self.df, df2, axis, **kwargs)
        return self

    def filtr(self, req=None, limit=None, random=False, seed=123):
        self.df = filtr_(self.df, req, limit, random, seed)
        return self

    def join(self, df2, on=None, type_join="inner", **kwargs):
        assert isinstance(df2, pd.DataFrame), "'df2' must be a data frame"
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
    
    def write(self, output, conn=None, db=None, **kwargs):            
        
        if output[-3:] == "csv":
        
            self.df.to_csv(path_or_buf=output, **kwargs)                                
        
        else:
            
            if conn is None:

                try:  # sql               
        
                    self.df.to_sql(output, con = self.conn, 
                                   if_exists = 'fail', **kwargs)
                                
                except: # mongo db
                
                    data = self.df.to_dict(orients='records')
                
                    exec("self.conn." + self.db[output] + ".insert_many(data)")
                                
            else:
                
                try:  # sql               
        
                    self.df.to_sql(output, con = conn, 
                                   if_exists = 'fail', **kwargs)
                                
                except: # mongo db
                
                    data = self.df.to_dict(orients='records')
                
                    exec("conn.db[" + output + "].insert_many(data)")
                                    
            
        
        
        