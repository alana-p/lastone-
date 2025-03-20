
import pandas as pd
import numpy as np



# Load the dataset
input_file = 'dirtydata.csv'
data = pd.read_csv(input_file)

# Inspect the dataset
print(data.head())
print(data.info())

# Clean the dataset: Replace '*' and '$' with an empty string
data = data.replace({'\%': ''}, regex=True)

# Drop unnecessary columns
if 'Name' in data.columns:
    data = data.drop('Name', axis=1)
if 'Extracurricular_Activities' in data.columns:
    data = data.drop('Extracurricular_Activities', axis=1)



# Output the cleaned data to a new CSV file
output_file = 'cleaned.csv'




#Define non-numeric cols:
non_numeric_cols = ['Gender','Department','Internet_Access_at_Home','Grade']

#Create a dictionary called stats_dictionary
stats_dictionary = {}

for col in data.columns:
    if col not in non_numeric_cols:
        stats_data = pd.to_numeric(data[col], errors='coerce')
        
        stats_dictionary[col] = {
            'Mean'   : stats_data.mean(),
            'Median' : stats_data.median(),
            'Mode'   : stats_data.mode().iloc[0] if not stats_data.mode().empty else np.nan,
            'Range'  : stats_data.max() - stats_data.min()
            }
print(stats_dictionary)

#Tidy up stats dictionary
stats_df = pd.DataFrame(stats_dictionary).transpose()
print(stats_df)




