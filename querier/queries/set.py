# Authors: Thierry Moudiki
#
# License: BSD 3 Clause Clear


import numpy as np
import pickle
import warnings

warnings.filterwarnings("ignore")

def setwhere(df, col, val, replace, copy=False):
    """ Set value.
   
       Parameters
       ----------
       df: a data frame
           a data frame
       
       col: str
           column to be filtered on
       
       val: object
           value to be replaced in column `col`
           
       replace: object
           replacement value
       
       copy: bool
           If True, a new data frame is created else input data frame is modified (default False)
       
       Examples
       --------
       
       https://github.com/thierrymoudiki/querier/tree/master/querier/demo
   
    """
    
    if copy is True:        
        df_ = pickle.loads(pickle.dumps(df, -1))
        df_[col][np.where(df[col] == val)[0]] = replace       
        return df_
    
    # copy == False:    
    df[col][np.where(df[col] == val)[0]] = replace       
    return df