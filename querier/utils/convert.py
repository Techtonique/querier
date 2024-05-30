import pandas as pd 
import polars as pl 

def pandas_to_polars(df):
    """ Convert a pandas data frame to a polars data frame.
    
    Args:
        
        df: a pandas data frame
            a pandas data frame
        
    """
    assert isinstance(df, pd.DataFrame), "df must be a pandas data frame"
    return pl.from_pandas(df)

def polars_to_pandas(df):
    """ Convert a polars data frame to a pandas data frame.
    
    Args:
        
        df: a polars data frame
            a polars data frame
        
    """
    assert isinstance(df, pl.DataFrame), "df must be a polars data frame"
    return df.to_pandas()