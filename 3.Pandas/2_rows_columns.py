import pandas as pd
import os

os.system("wget https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/tf2.0/sbux.csv")

df = pd.read_csv('sbux.csv', error_bad_lines=False)
os.system("clear")
print(df.columns)

#change Name to lowercase: 

df.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'name']
print(df.columns)

#print a specific column
print(df[['open', 'close']])

#if it was df[open] it would be a series, however when there are two attributes, this is a data frame type

#using iloc to access the rows: 

print(df.iloc[0])







os.system("rm sbux.csv")