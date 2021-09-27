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

print(df.loc[0])
# print(df.iloc[0])
#using date as the index of the dataset
df2= pd.read_csv('sbux.csv', index_col = 'date')
print(df2.head(2))

#we now can access the data with the date
print(df2.loc['2013-02-08'])

#access all rows where the open price was above 64
print(df[df['open'] > 64])

#creating a new csv
smalldf = df[['open','close']]
smalldf.to_csv('output.csv')

print(smalldf.head(2))

# To remove the index column 
smalldf2 = df[['open','close']]
smalldf2.to_csv('output2.csv', index=False)

print(smalldf2.head(2))



#cleaning up
os.system("rm sbux.csv output.csv output2.csv")