![querier logo](the-querier.png)

<hr>  

Data Frames are widely used and useful structures for data wrangling. The `querier`  exposes a query language for Python `pandas` Data Frames, inspired from SQL's relational databases querying logic. 

![PyPI](https://img.shields.io/pypi/v/querier) [![PyPI - License](https://img.shields.io/pypi/l/querier)](https://github.com/thierrymoudiki/querier/blob/master/LICENSE) [![Downloads](https://pepy.tech/badge/querier)](https://pepy.tech/project/querier) [![Documentation Status](https://readthedocs.org/projects/querier/badge/?version=latest)](https://querier.readthedocs.io/en/latest/?badge=latest)
 

## Contents 
 [Installation](#Installation) |
 [Package description](#package-description) |
 [Contributing](#Contributing) |
 [Tests](#Tests) |
 [API Documentation](#api-documentation) |
 [Dependencies](#dependencies) |
 [License](#License) 

## Installation 

- From Pypi: 

```bash
pip install querier 
```

- From Github, for the development version: 

```bash
pip install git+https://github.com/thierrymoudiki/querier.git
```

## Package description

There are currently __9 types of operations__ available in the `querier`, with no plan to extend that list much further (to maintain a relatively simple mental model). These verbs will look familiar to `dplyr` users, but the implementation (I used `numpy`, `pandas` and `SQLite3`) and functions' signatures are different: 

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

- [`concat` example](/querier/demo/thierrymoudiki_251019_concat.ipynb)
- [`delete` example](/querier/demo/thierrymoudiki_241019_delete.ipynb)
- [`drop` example](/querier/demo/thierrymoudiki_241019_drop.ipynb)
- [`filtr` example](/querier/demo/thierrymoudiki_231019_filtr.ipynb)
- [`join` example](/querier/demo/thierrymoudiki_231019_join.ipynb)
- [`select` example](/querier/demo/thierrymoudiki_231019_select.ipynb)
- [`summarize` example](/querier/demo/thierrymoudiki_231019_summarize.ipynb)
- [`update` example](/querier/demo/thierrymoudiki_251019_update.ipynb)
- [`request` example](/querier/demo/thierrymoudiki_231019_request.ipynb)



## Contributing

Your contributions are welcome, and valuable. Please, make sure to __read__ the [Code of Conduct](CONTRIBUTING.md) first. 

If you're not comfortable with Git/Version Control yet, please use [this form](https://forms.gle/uStfcXJjtGki2R3s6).

In Pull Requests, let's strive to use [`black`](https://black.readthedocs.io/en/stable/) for formatting: 

```bash
pip install black
black --line-length=80 file_submitted_for_pr.py
```

## Tests

TBD

## API documentation

[https://querier.readthedocs.io/en/latest/](https://querier.readthedocs.io/en/latest/)

## Dependencies 

- Numpy
- Pandas
- SQLite3


## License

[BSD 3-Clause](LICENSE) © Thierry Moudiki, 2019. 

