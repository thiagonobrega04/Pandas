import pandas as pd

# Let's create a DataFrame for our grocery list
grocery_items = {'Items': ['Milk', 'Bread', 'Cheese', 'Butter'], 
                 'Price': [2.5, 1.5, 3.5, 2.0]}
grocery_df = pd.DataFrame(grocery_items)

# Now let's add a new item 'Honey' to our grocery list
new_item = pd.DataFrame({'Items': ['Honey'], 'Price': [4.0]})
grocery_df = pd.concat([grocery_df, new_item]).reset_index(drop=True)

# But we decided we don't need 'Cheese'. Let's remove it from our list
index_to_drop = grocery_df[grocery_df['Items'] == 'Cheese'].index
grocery_df = grocery_df.drop(index_to_drop)

print(grocery_df)

# create a DataFrame for a grocery list
data = {
    'Item': ['Milk', 'Eggs', 'Bread', 'Butter'],
    'Quantity': [2, 12, 1, 1]
}

grocery_df = pd.DataFrame(data)

# add a new row for 'Spinach'
new_row = pd.DataFrame({'Item': ['Spinach'], 'Quantity': [5]})

grocery_df = pd.concat([grocery_df, new_row]).reset_index(drop=True)

# remove 'Milk' from the list
item_to_remove = grocery_df[grocery_df['Item'] == 'Milk'].index

grocery_df = grocery_df.drop(item_to_remove)

print(grocery_df)

grocery_items = {
    'Item': ['Eggs', 'Bread', 'Cheese', 'Butter'],
    'Quantity': [12, 1, 1, 1]
}

grocery_df = pd.DataFrame(grocery_items)

new_items = pd.DataFrame({
    'Item': ['Milk', 'Yogurt'], 
    'Quantity': [2, 3]
})

grocery_df = pd.concat([grocery_df, new_items]).reset_index(drop=True)

item_to_drop = grocery_df[grocery_df['Item'] == 'Cheese'].index
grocery_df = grocery_df.drop(item_to_drop)

print(grocery_df)

# We will create a DataFrame for our grocery list
grocery_items = {'Items': ['Peas', 'Squash', 'Tomatoes', 'Onions'], 
                 'Price': [1.0, 1.5, 2.5, 0.75]}
grocery_df = pd.DataFrame(grocery_items)

# Now let's add new items to our grocery list
new_items = pd.DataFrame({
    'Items': ['Cucumber', 'Radish'], 
    'Price': [0.50, 0.30]
})
# TODO: Create a DataFrame with two new items 'Cucumber' priced at $0.50 and 'Radish' priced at $0.30
grocery_df = pd.concat([grocery_df, new_items]).reset_index(drop=True)

# TODO: Concat the new items DataFrame with the current grocery DataFrame and update it

print(grocery_df)

# Let's begin by creating a DataFrame for our grocery list
grocery_items = {'Grocery Item': ['Peas', 'Squash', 'Tomatoes', 'Onions', 'Apples', 'Oranges'],
                 'Price': [1.0, 1.5, 2.5, 0.75, 0.65, 0.5]}
grocery_df = pd.DataFrame(grocery_items)

# Now, let's remove certain items from our grocery list
items_to_remove = grocery_df[grocery_df['Grocery Item'].isin(['Apples', 'Oranges'])].index
grocery_df = grocery_df.drop(items_to_remove)

# TODO: Find indices of 'Apples' and 'Oranges' in the DataFrame
# TODO: Use the dataframe.drop() function to remove these items by their indices

print(grocery_df)