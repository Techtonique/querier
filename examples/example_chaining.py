# Authors: Thierry Moudiki
#
# License: BSD 3

import pandas as pd
import querier as qr


# Import data -----

url = ('https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv')
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