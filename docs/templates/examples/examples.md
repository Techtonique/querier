#  Example

Here is an example for chaining operations in the __querier__. Multiple other examples can be found [in these notebooks](https://github.com/Techtonique/querier/tree/master/querier/demo). 

```python

import pandas as pd
import querier as qr


# Import data -----

url = ('https://raw.github.com/pandas-dev'
   '/pandas/master/pandas/tests/data/tips.csv')
df = pd.read_csv(url)


# Example 1 -----

qrobj = qr.Querier(df=df)

df1 = qrobj\
.select(req="tip, sex, smoker, time")\
.filtr(req="smoker == 'No'")\
.summarize(req="sum(tip), sex, time", group_by="sex, time")\
.df

print(df1)


# Example 2 -----

df2 = qr.Querier(df)\
.select(req='tip, sex, day,size')\
.filtr(req="(day == 'Sun') | (day == 'Sat')")\
.summarize(req="avg(tip), sex, day", group_by="sex, day")\
.df

print(df2)

```