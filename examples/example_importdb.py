# Authors: Thierry Moudiki
#
# License: BSD 3

import pandas as pd
import querier as qr
import sqlite3 
import sys


# data -----

url = ('https://raw.github.com/pandas-dev'
   '/pandas/master/pandas/tests/data/tips.csv')


# Example 1 - Import from csv -----

qrobj1 = qr.Querier(source=url)

df1 = qrobj1\
.select(req="tip, sex, smoker, time")\
.filtr(req="smoker == 'No'")\
.summarize(req="sum(tip), sex, time", group_by="sex, time")\
.df

print(df1)


# Example 2 - Import from sqlite3 -----

# an sqlite3 database  connexion
con = sqlite3.connect('people.db')
 
with con:
    cur = con.cursor()    
    cur.execute("CREATE TABLE Population(id INTEGER PRIMARY KEY, name TEXT, age INT, sex TEXT)")
    cur.execute("INSERT INTO Population VALUES(NULL,'Michael',19, 'M')")
    cur.execute("INSERT INTO Population VALUES(NULL,'Sandy', 41, 'F')")
    cur.execute("INSERT INTO Population VALUES(NULL,'Betty', 34, 'F')")
    cur.execute("INSERT INTO Population VALUES(NULL,'Chuck', 12, 'M')")
    cur.execute("INSERT INTO Population VALUES(NULL,'Rich', 24, 'M')")
    
# create querier object from sqlite3 database 
qrobj2 = qr.Querier(source='people.db', table="Population")    

# people with age >= 20
df2 = qrobj2.select(req="name, age, sex").filtr(req="age >= 20").df
print(df2)

# avg. age for people with age >= 20, group by sex
qrobj3 = qr.Querier(source='people.db', table="Population")  
df3 = qrobj3.select(req="name, age, sex").filtr(req="age >= 20")\
.summarize("avg(age), sex", group_by="sex").df

print(df3)