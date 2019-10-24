![querier logo](the-querier.png)

<hr>  

Data Frames are widely used and useful structures for data wrangling. The `querier`  exposes a query language for Python `pandas` Data Frames, inspired from SQL's relational databases querying logic. 

## Installation 

- Currently from Github, for the development version: 

```bash
pip install git+https://github.com/thierrymoudiki/querier.git
```

## Package description

There are currently __9 types of operations__ available in the `querier`, with no plan to extend that list much further (to maintain a relatively simple mental model). These verbs will look familiar to `dplyr` users, but the implementation (I used `numpy`, `pandas` and `SQLite3`) and signatures are different: 

- `concat`: __concatenates 2 Data Frames__, either horizontally or vertically
- `delete`: __deletes rows__ from a Data Frame based on given criteria
- `drop`: __drops columns__ from a Data Frame
- `filtr`: __filters rows__ of the Data Frame based on given criteria
- `join`: __joins 2 Data Frames__ based on given criteria (available for _completeness_ of the interface, this operation is already straightforward in pandas)
- `select`: __selects columns__ from the Data Frame
- `summarize`: obtains __summaries of data__ based on grouping columns
- `update`: __updates a column__, using an operation given by the user
- `request`: for operations more complex than the previous 8 ones, makes it possible to use a __SQL query on the Data Frame__

The following notebooks present __examples of use__ of the `querier`: 

- [`select` example](/querier/demo/thierrymoudiki_231019_select.ipynb)
- [`filtr` example](/querier/demo/thierrymoudiki_231019_filtr.ipynb)
- [`summarize` example](/querier/demo/thierrymoudiki_231019_summarize.ipynb)
- [`join` example](/querier/demo/thierrymoudiki_231019_join.ipynb)
- [`request` example](/querier/demo/thierrymoudiki_231019_request.ipynb)
- [`delete` example](/querier/demo/thierrymoudiki_241019_delete.ipynb)
- [`drop` example](/querier/demo/thierrymoudiki_241019_drop.ipynb)


## Contributing

Your contributions are welcome, and valuable. Please, make sure to __read__ the [Code of Conduct](CONTRIBUTING.md) first. In Pull Requests, let's strive to use [`black`](https://black.readthedocs.io/en/stable/) for formatting: 

```bash
pip install black
black --line-length=60 file_submitted_for_pr.py
```

## Dependencies 

- Numpy
- Pandas
- SQLite3

## License

[BSD 3-Clause](LICENSE) © Thierry Moudiki, 2019. 

