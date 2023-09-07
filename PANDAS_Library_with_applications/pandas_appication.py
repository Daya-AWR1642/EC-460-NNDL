import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd 
from pandas import DataFrame , read_csv
#%matplotlib inline


# creating a dictionary
d = {'one' : pd.Series([1.,2.,3.,4.0] , index = ['a','b','c','d']),
     'two' : pd.Series([1.,2.,3.,4.0], index = ['a','b','c','d'])}
# creating Data frame
df = pd.DataFrame(d)
print(df)
print(df.shape)
print(df.dtypes)

# creating the Data Range
dates = pd.date_range('20230828', periods = 10)
print(dates)


df2 = pd.DataFrame(np.random.randn(10,5),index = dates, columns = list('ABCDE'))
print(df2.head())

# THE data merging example

names = ['Bob','Jessica','Marry','John','Mel']
births = [968,155,77,578,973]

# To merge  these two lists  together  we will use  the zip function

BabyDataSet = list(zip(names,births))
print(BabyDataSet)

# PANDAS  CREATE A DATA FRAME AND WRITE  TO CSV FILE

df3 = pd.DataFrame(data = BabyDataSet, columns = ['Names','Births'])
#df3.to_csv('Births1880.csv', index = False, header = False)
df3.to_csv('/home/dayananda/Documents/NNDL/PANDAS_Library_with_applications/Births1880_anotherway.csv',index = False, header = False)


# READING THE DATA FROM CSV FILE
"""
- df = pd.read_csv(filename)
- Don't  treat  the first row as header 
-  df = pd.read_csv(Location,header = None)
- Provide specific name  for columns
- df = pd.read_csv(Locatoin, names = ['Names','Births'])
"""


