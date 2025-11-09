# Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.

# Populate your new table with the following values:
# Display the Name and Age of everyone in the table classified as Bajoran.
import pandas as pd 
data = {'Name': ['Benjamin Sisko','Jadzia Dax','Kira Nerys'],
        'Species':['Human','Trill','Bajoran'],
        'Age':[40,300,29]}

df = pd.DataFrame(data)

bajoran = df[df['Species'] == 'Bajoran'][['Name','Age']]

print(bajoran)
