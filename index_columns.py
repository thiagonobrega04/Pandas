import pandas as pd

data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "City": ["New York", "Paris", "Berlin", "London"]
}

df = pd.DataFrame(data)

print(df)

df['ID'] = [101, 102, 103, 104]    # Adding unique IDs
df.set_index('ID', inplace=True)   # Setting 'ID' as index

print(df)

df.reset_index(inplace=True)       # Resetting index

print(df)

df = pd.DataFrame(data)
df['ID'] = [101, 102, 103, 104]    # Adding unique IDs
df.set_index('ID', inplace=True)   # Setting 'ID' as index

print(df.loc[102])
print(df.loc[[102, 104]])
print(df.loc[[102, 104], ['Name', 'Age']]) # Selecting Multiple Columns with `loc`
print(df.loc[:, ['Name', 'Age']]) # select all rows for specific columns, providing : as a set of index labels
print(df.iloc[3]) # Using `iloc` for Location by Index Position
print(df.iloc[1:3]) # using slicing here