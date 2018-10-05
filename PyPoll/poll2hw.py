# Dependencies
import pandas as pd 
    
# Save path to data set in a variable
data_file = "electiondata.csv" 

# Use Pandas to read data
data_file_pd = pd.read_csv(data_file)
data_file_pd.head()
