import pandas as pd

data = {
    'Grocery Item': ['Apples', 'Oranges', 'Bananas', 'Grapes'],
    'Price per kg': [3.25, 4.50, 2.75, 5.00]
}

grocery_df = pd.DataFrame(data)

print(grocery_df)

new_row = pd.DataFrame({'Grocery Item': ['Pears'], 'Price per kg': [4.00]})

grocery_df = pd.concat([grocery_df, new_row]).reset_index(drop=True)

print(grocery_df)

new_rows = pd.DataFrame({
    'Grocery Item': ['Avocados', 'Blueberries'],
    'Price per kg': [2.5, 10.0]
})

grocery_df = pd.concat([grocery_df, new_rows]).reset_index(drop=True)

print(grocery_df)

index_to_delete = grocery_df[grocery_df['Grocery Item'] == 'Grapes'].index

grocery_df = grocery_df.drop(index_to_delete)

print(grocery_df)

indices_to_delete = grocery_df[grocery_df['Grocery Item'].isin(['Apples', 'Oranges'])].index

grocery_df = grocery_df.drop(indices_to_delete)

print(grocery_df)