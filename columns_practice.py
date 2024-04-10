import pandas as pd

people = {
    "Name": ["Austin", "Emma", "Ethan", "Sophia"],
    "Age": [22, 28, 35, 30],
    "City": ["Chicago", "Boston", "San Francisco", "Los Angeles"]
}

df = pd.DataFrame(people)

df['ID'] = [201, 202, 203, 204]
df.set_index('ID', inplace=True)

print(df.loc[:, ['Name', 'Age']])

people = {
    "Name": ["Mike", "Emily", "Nick", "Chloe"],
    "Age": [22, 28, 30, 26],
    "City": ["Toronto", "Vancouver", "Ottawa", "Montreal"]
}

df = pd.DataFrame(people)

df['ID'] = [301, 302, 303, 304]
df.set_index('ID', inplace=True)

# TODO: Change to select the last two rows
last_two = df.iloc[-2:]
print(df.iloc[2:4])

people = {
    "Name": ["Lucas", "Mia", "Jack", "Sophie"],
    "Age": [21, 29, 32, 25],
    "City": ["Dublin", "Cork", "Galway", "Limerick"]
}

df = pd.DataFrame(people)

df['ID'] = [701, 702, 703, 704]
df.set_index('ID', inplace=True)

# Selecting all rows for 'Name' and 'City' columns  
print(df.loc[:, ['Name', 'City']])

people = {
    "Name": ["Charlie", "Oliver", "Sophie", "Lucas"],
    "Age": [33, 27, 36, 38],
    "City": ["Toronto", "Vancouver", "Ottawa", "Montreal"]
}

df = pd.DataFrame(people)
df['ID'] = [501, 502, 503, 504]
df.set_index('ID', inplace=True)

# TODO: Print the details of the person with ID 503
print(df.loc[503])