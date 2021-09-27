import pandas as pd
import os

os.system("wget https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/tf2.0/sbux.csv")

df = pd.read_csv('sbux.csv', error_bad_lines=False)
os.system("clear")
print(type(df))
# os.system("head sbux.csv")
print(df.head(2))
print(df.tail(2))
print(df.info())
os.system("rm sbux.csv")
