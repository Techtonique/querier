# Querier

<span style="float:right;">[[source]](https://github.com/Techtonique/querier/querier/wrapper/wrapper.py#L27)</span>

### Querier


```python
querier.Querier(df=None, source=None, db=None, table=None, **kwargs)
```


A wrapper for chaining the querier's atomic operations, which are currently:
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
   


----

