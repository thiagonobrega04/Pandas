import pandas as pd

student_data = {  
    'Name': ['Sara', 'Ray', 'John'],
    'Age': [15, 16, 17],
}

df = pd.DataFrame(student_data)

df['Grade'] = [9, 10, 7]
print(df.index)  # Output: RangeIndex(start=0, stop=3, step=1)
print(df.columns)  # Output: Index(['Name', 'Age', 'Grade'], dtype='object') 

print(df)
print(df['Name'])
print(df[['Name','Grade']])
print(df.dtypes)
