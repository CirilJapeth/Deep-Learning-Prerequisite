import pandas as pd
import os
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix


def date_to_year(row): 
    return int(row['date'].split('-')[0])
    # from data frame row get date that is split with - and take the 0th item

#Get the data frame and assign df to it
os.system("wget https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/tf2.0/sbux.csv")

df = pd.read_csv('sbux.csv', error_bad_lines=False)
os.system("clear")
#--------------------------------------

#create a histogram
df['open'].hist()
plt.show()

#create a linegraph
df['open'].plot()
plt.show()

#box plot
df[['open', 'high', 'low', 'close']].plot.box()
plt.show()

#scatter matrix
scatter_matrix(df[['open', 'high', 'low', 'close']],
               alpha = 0.2, figsize=(6,6));
#alpha = 0.2 makes the dots have transpirancy and figsize makes the plot a little bigger
plt.show()

os.system("rm sbux.csv")