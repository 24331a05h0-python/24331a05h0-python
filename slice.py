import pandas as pd

data = {
    'Name': ['Rahul', 'Anitha', 'Kiran', 'Sneha', 'Vijay'],
    'Age': [21, 22, 20, 23, 21],
    'Marks': [85, 90, 78, 88, 80]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

sorted_df = df.sort_values(by='Marks')
print("\nSorted by Marks")
print(sorted_df)

print("\nSliced rows (0 to 3)")
print(df[0:3])

print("\nSelecting Name and Marks columns")
print(df[['Name','Marks']])
