# Verbs

_In alphabetical order_

<span style="float:right;">[[source]](https://github.com/Techtonique/querier/blob/master/querier/queries/concat.py#L16)</span>

### concat


```python
querier.concat(df1, df2, axis="h", **kwargs)
```


Concatenate data frames.
   
Args:           
    
    df1: a data frame
        a data frame
       
    df2: a data frame           
        a data frame
       
    axis: str
        specify the type of concatenation: "h"=horizontal, "v"=vertical
                             
Examples:
       
    https://github.com/thierrymoudiki/querier/tree/master/querier/demo
   


----

<span style="float:right;">[[source]](https://github.com/Techtonique/querier/blob/master/querier/queries/delete.py#L13)</span>

### delete


```python
querier.delete(df, req=None)
```


Delete rows from a data frame.
   
Args:           
    
    df: a data frame 
        a data frame
           
    req: str
        criteria for filtering the rows to be deleted
                             
Examples:    
       
    https://github.com/thierrymoudiki/querier/tree/master/querier/demo
   


----

<span style="float:right;">[[source]](https://github.com/Techtonique/querier/blob/master/querier/queries/drop.py#L9)</span>

### drop


```python
querier.drop(df, req=None)
```


Drop columns.
   
Args: 
   
    req: str
        comma-separated list of columns to be dropped
                 
Examples:     
   
    https://github.com/thierrymoudiki/querier/tree/master/querier/demo
   


----

<span style="float:right;">[[source]](https://github.com/Techtonique/querier/blob/master/querier/queries/filtr.py#L27)</span>

### filtr


```python
querier.filtr(df, req=None, limit=None, random=False, seed=123)
```


Filter rows, based on given criteria.

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


----

<span style="float:right;">[[source]](https://github.com/Techtonique/querier/blob/master/querier/queries/join.py#L21)</span>

### join


```python
querier.join(df1, df2, on=None, type_join="inner", **kwargs)
```


Join data frames.

Args:

    df1: a data frame           
       a data frame
   
    df2: a data frame           
       a data frame
   
    on: str
       joining column/criterion
   
    type_join: str           
       type of join. Options are: "left", "right", "outer", "inner". 
       Default is "inner" join.              
   
Examples: 
   
    https://github.com/thierrymoudiki/querier/tree/master/querier/demo


----

<span style="float:right;">[[source]](https://github.com/Techtonique/querier/blob/master/querier/queries/request.py#L20)</span>

### request


```python
querier.request(df, req=None, **kwargs)
```


SQL request on a data frame.
   
Args:           

    df: a data frame
        a data frame
       
    req: str
        specifying the SQL request
                  
       
Examples:           
       
    https://github.com/thierrymoudiki/querier/tree/master/querier/demo
   


----

<span style="float:right;">[[source]](https://github.com/Techtonique/querier/blob/master/querier/queries/select.py#L17)</span>

### select


```python
querier.select(df, req="*", order_by=None, asc=True, limit=None, random=False, seed=123)
```


Select columns.
   
Args:

    df: a data frame
        a data frame
    
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
   


----

<span style="float:right;">[[source]](https://github.com/Techtonique/querier/blob/master/querier/queries/set.py#L12)</span>

### setwhere


```python
querier.setwhere(df, col, val, replace, copy=False)
```


Set value.

Args:
   
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
   
Examples: 
   
    https://github.com/thierrymoudiki/querier/tree/master/querier/demo


----

<span style="float:right;">[[source]](https://github.com/Techtonique/querier/blob/master/querier/queries/summarize.py#L10)</span>

### summarize


```python
querier.summarize(df, req=None, group_by=None, having=None, **kwargs)
```


Data summaries on rows.
   
Args:           

    df: a data frame
        a data frame
           
    req: str
        specifying the aggregating operations on columns
       
    group_by: str
            comma-separated list of columns to be aggregated
       
    having: str
           filtering criterion on groups
       
Examples:
       
    https://github.com/thierrymoudiki/querier/tree/master/querier/demo
   


----

<span style="float:right;">[[source]](https://github.com/Techtonique/querier/blob/master/querier/queries/update.py#L13)</span>

### update


```python
querier.update(df, req=None)
```


Update the data frame.

Args:           

    df: a data frame
        a data frame
   
    req: str
        specifying the transformation, e.g `new_size = 3*size`
             
Examples: 

    https://github.com/thierrymoudiki/querier/tree/master/querier/demo


----

