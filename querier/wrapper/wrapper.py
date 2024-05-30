"""Wrapper for the querier's operations."""

# Authors: Thierry Moudiki
#
# License: BSD 3


import pandas as pd
import polars as pl
import sqlite3
from pymongo import MongoClient
from ..utils import polars_to_pandas, pandas_to_polars
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
    setwhere as setwhere_,
)


class Querier(object):
    """ A wrapper for chaining the querier's atomic operations, which are currently:
       `concat`, `delete`, `drop`, `filtr`, `join`, `select`, `summarize`,
       `update`, `request`
       
    Attributes: 
       
        df: a data frame
            a data frame (optional)
           
        source: str
            a csv file path, sql database path, or mongo db uri
                 
        db: str
            database name, if `source` is a mongo db uri
                 
        table: str
            name of the table/collection, if `source` is provided and is a database
           
    Examples:
       
        https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
    """

    def __init__(self, df=None, source=None, db=None, table=None, **kwargs):

        if (df is not None):

            assert (source is None) & (
                table is None
            ), "No `source` required when `df` is provided"

            self.df = df

        elif source is not None:

            assert df is None, "`df` is no used when `source` is provided"

            self.source = source

            if self.source[-3:] == "csv":

                self.df = pd.read_csv(self.source, **kwargs)

            elif self.source[0:7] == "mongodb":

                assert (table is not None) & (
                    isinstance(table, str)
                ), "`table` name must be (a string) provided along with database `source`"

                assert (db is not None) & (
                    isinstance(db, str)
                ), "A database `db` must be provided"

                self.table = table
                self.conn = MongoClient(self.source, **kwargs)
                self.db = self.conn[db]
                self.df = pd.DataFrame(list(self.db[table].find()))

            else:  # other db source

                assert (table is not None) & (
                    isinstance(table, str)
                ), "`table` name must be (a string) provided along with db `source`"

                self.table = table

                try:

                    self.df = pd.read_sql_table(
                        table_name=self.table, con=self.source, **kwargs
                    )

                except:

                    try:  # sqlite3 source

                        self.conn = sqlite3.connect(self.source, **kwargs)
                        self.df = pd.read_sql_query(
                            "SELECT * FROM " + self.table,
                            con=self.conn,
                            **kwargs
                        )

                    except:

                        raise ValueError("Database format not supported")

        else:

            raise ValueError("Check database format provided in `source`")

        self.colnames = self.df.columns.values
        self.rownames = self.df.index.values
        self.nrows = self.df.shape[0]
        self.ncols = self.df.shape[1]
        self.dtypes = self.df.dtypes.values
    
    
    def get_df(self, return_values=False):
        """ Get object's data frame attribute.
       
        Args:          

            return_values: bool
                If True, a numpy array is returned. Otherwise, a data frame (default).
           
        Examples:
           
            https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
       """

        if return_values:
            return self.df.values
        return self.df    

    def set_df(self, df):
        """ Set object's data frame attribute.
       
        Args:           
        
            df: A data frame
                the data frame to be concatenated to our existing data 
                      
        Examples:
           
            https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
       """
        
        self.df = df                

    def select(
        self,
        req="*",
        order_by=None,
        asc=True,
        limit=None,
        random=False,
        seed=123,
    ):
        """ Select columns.
       
        Args:

            req: str
            comma-separated columns names
        
            order_by: str
            sort the results by using these columns (optional)
        
            asc: bool
            if `order_by` is provided, `True` means: ascending ordering 
        
            limit: int
            number of records to be retrieved 
        
            random: bool
            `True` if we want a random set of records 
        
            seed: int
            reproducibility seed for situations where `random == True`
       
        Examples:
       
            https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
        """

        self.df = select_(self.df, req, order_by, asc, limit, random, seed)
        return self

    def update(self, req=None):
        """ Update the data frame.
       
        Args:  

            req: str
               specifying the transformation, e.g `new_size = 3*size`
                      
           
        Examples: 
           
            https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
       """
        self.df = update_(self.df, req)
        return self

    def delete(self, req=None):
        """ Delete rows from the data frame.
       
        Args:

            req: str
               criteria for filtering the rows to be deleted
                      
           
        Examples: 
           
            https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
       """
        self.df = delete_(self.df, req)
        return self

    def concat(self, df2, axis="h", **kwargs):
        """ Concatenate data frames.
       
        Args:           
        
            df2: A data frame
               the data frame to be concatenated to our existing data 
           
            axis: str
               specify the type of concatenation: "h"=horizontal, "v"=vertical
                                 
        Examples: 
           
            https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
       """

        assert isinstance(df2, pd.DataFrame), "'df2' must be a data frame"
        self.df = concat_(self.df, df2, axis, **kwargs)
        return self

    def filtr(self, req, limit=None, random=False, seed=123):
        """ Filter rows, based on given criteria.
       
        Args:           
        
            req: str
               criteria for filtering the rows

            limit: int
               number of records to be retrieved 
        
            random: bool
               `True` if we want a random set of records 
           
            seed: int
               reproducibility seed for situations where `random == True`
                                 
        Examples:            

            https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
       """

        self.df = filtr_(self.df, req, limit, random, seed)
        return self

    def join(self, df2, on=None, type_join="inner", **kwargs):
        """ Join data frames into our existing data frame.
       
        Args:           
        
            df2: A data frame
                the data frame to be joined to our existing data 
           
            on: str
               joining column/criterion
           
           type_join: str           
               type of join. Options are: "left", "right", "outer", "inner". 
               Default is "inner" join.       
           
           
        Examples:        
           
            https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
       """
        self.df = join_(self.df, df2, on, type_join, **kwargs)
        return self

    def summarize(self, req, group_by=None, having=None, **kwargs):
        """ Data summaries on rows.
       
        Args:           
            
            req: str
               specifying the aggregating operations on columns
           
            group_by: str
               comma-separated list of columns to be aggregated
           
            having: str
               filtering criterion on groups
           
        Examples:           
           
            https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
       """

        self.df = summarize_(self.df, req, group_by, having, **kwargs)
        return self

    def drop(self, req):
        """ Drop columns.
       
        Args:           
        
            req: str
               comma-separated list of columns to be dropped                      
           
        Examples:
           
            https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
       """

        self.df = drop_(self.df, req)
        return self

    def request(self, req, **kwargs):
        """ SQL request on the data frame.
       
        Args:           
        
            req: str
                specifying the SQL request
                                 
        Examples:           
           
            https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
       """

        self.df = request_(self.df, req, **kwargs)
        return self

    def setwhere(self, col, val, replace):
        """ Set value.
       
        Args:           
            
            col: str
               column to be filtered on
           
            val: object
               value to be replaced in column `col`
               
            replace: object
               replacement value
           
            copy: bool
               If True, a new data frame is created else input data frame is modified (default False)
           
        Examples:
           
            https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
        """

        self.df = setwhere_(self.df, col=col, val=val, 
                            replace=replace, copy=False)
        return self

    def write(self, output, conn=None, db=None, **kwargs):
        """ Export data frame's content to csv file or database.
       
        Args:           
        
            output: str
                    csv file path, sql table name, mongo db collection name
           
            conn: a database connexion
                database connexion (optional). Default: use the current object's 
                connexion, if provided. 
           
            db: str
               collection name (optional), if `conn` is a mongo db connexion
           
        Examples:
           
            https://github.com/thierrymoudiki/querier/tree/master/querier/demo
       
       """

        if output[-3:] == "csv":

            self.df.to_csv(path_or_buf=output, **kwargs)

        else:

            if conn is None:

                try:  # sql

                    self.df.to_sql(
                        output, con=self.conn, if_exists="fail", **kwargs
                    )

                except:  # mongo db

                    records = self.df.to_dict(orients="records")

                    exec(
                        "self.conn." + self.db[output] + ".insert_many(records)"
                    )

            else:

                try:  # sql

                    self.df.to_sql(output, con=conn, if_exists="fail", **kwargs)

                except:  # mongo db

                    records = self.df.to_dict(orients="records")

                    exec("conn.db[" + output + "].insert_many(records)")
