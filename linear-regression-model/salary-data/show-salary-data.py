### In this file, we will show the salary data in a table format. ###
### The source code here can also be used in jupyter notebook for a more clear user interface of the data table. ###

#this imports the whole pandas library and renames it to pd
# The pandas library is used for working with outside data such csv files, excel files, image-captures, and databases.
# pandas is also used for manupulating dataframes, series, and has additional data structures.
import pandas as pd


# Specify the file path of the CSV file
file_path = 'salary-data-2022.csv'

# Read the CSV file and store it in a DataFrame
df = pd.read_csv(file_path)

my_df = pd.DataFrame(df)
print(my_df)