import pandas as pd
import numpy as np

data = {
    'Name': ['Rahul','Anitha','Kiran','Sneha','Vijay'],
    'Age': [21, np.nan, 20, 23, 22],
    'Marks': [85, 90, np.nan, 88, 80]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Marks'].fillna(0, inplace=True)

df['Marks'] = df['Marks'] + 5

df.rename(columns={'Marks':'Total Marks'}, inplace=True)

print("\nModified and Cleaned DataFrame")
print(df)
