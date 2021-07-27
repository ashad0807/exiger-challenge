import os
import pandas as pd

d = dict()
date = '2020-04-16'
iso = 'USA'
# d = {('2020-04-16', 'USA'): {'date': '2020-04-16', 'iso': 'USA', 'num_confirmed': 667801, 'num_deaths': 32916, 'num_recovered': 54703}, 'key2':'val2'}

# df = pd.DataFrame(merged_data.items(), columns=['date', 'iso', 'num_confirmed', 'num_deaths', 'num_recovered'])

d =  {'id': 'CS2_056', 'cost': 2, 'name': 'Tap'}
# df = pd.DataFrame([d], columns=d.keys())
df = pd.DataFrame({'col1': list(d.values()), 'col2': list(d.keys())})
print (df)

