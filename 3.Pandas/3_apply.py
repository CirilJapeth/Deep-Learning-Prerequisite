#here, we extract the year from the date and then create a seperate column to store it
import pandas as pd
import os

def date_to_year(row): 
    return int(row['date'].split('-')[0])
    # from data frame row get date that is split with - and take the 0th item

#Get the data frame and assign df to it
os.system("wget https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/tf2.0/sbux.csv")

df = pd.read_csv('sbux.csv', error_bad_lines=False)
os.system("clear")
#--------------------------------------


# apply the function we created to every single row
df['year'] = df.apply(date_to_year, axis =1); 
#axis = 1 to specify operation on row and not column

print(df.head(3))


#clean up
os.system("rm sbux.csv")
