"""Dropping columns"""

# Authors: Thierry Moudiki
#
# License: BSD 3


# creates a copy
def drop(df, req=None):      
    try:
        return df.drop(req.replace(" ", "").split(','), axis=1)
    except:
        raise ValueError('request must contain df''s column names (comma-separated)')
            
