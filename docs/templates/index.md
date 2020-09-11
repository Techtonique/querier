

# querier

![PyPI](https://img.shields.io/pypi/v/querier) [![PyPI - License](https://img.shields.io/pypi/l/querier)](https://github.com/thierrymoudiki/querier/blob/master/LICENSE) [![Downloads](https://pepy.tech/badge/querier)](https://pepy.tech/project/querier)

Welcome to __querier__'s website.

## Presentation

Data Frames are widely used and useful structures for data wrangling. The `querier`  exposes a query language for Python `pandas` Data Frames, inspired from SQL's relational databases querying logic. 

There are currently __9 main types of operations__ available in the `querier`, with no plan to extend that list much further (to maintain a relatively simple mental model). These verbs will look familiar to `dplyr` users, but the implementation (`numpy`, `pandas` and `SQLite3` is used) and functions' signatures are different: 

- `concat`: __concatenates 2 Data Frames__, either horizontally or vertically
- `delete`: __deletes rows__ from a Data Frame based on given criteria
- `drop`: __drops columns__ from a Data Frame
- `filtr`: __filters rows__ of the Data Frame based on given criteria
- `join`: __joins 2 Data Frames__ based on given criteria (available for _completeness_ of the interface, this operation is already straightforward in pandas)
- `select`: __selects columns__ from the Data Frame
- `summarize`: obtains __summaries of data__ based on grouping columns
- `update`: __updates a column__, using an operation given by the user
- `request`: for operations more complex than the previous 8 ones, makes it possible to use a __SQL query on the Data Frame__

## Installation 

- From Pypi: 

```bash
pip install querier 
```

- From Github, for the development version: 

```bash
pip install git+https://github.com/thierrymoudiki/querier.git
```
