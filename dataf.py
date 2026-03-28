import pandas as pd

df = pd.read_csv("students.csv")
print("Head:")
print(df.head())

print("\nTail:")
print(df.tail())

print("\nInfo:")
print(df.info())

print("\nDescribe:")
print(df.describe())
