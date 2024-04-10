import pandas as pd

classroom_data = {  
    'StudentName': ['Amy', 'Bob', 'Eva', 'Jake'], 
    'Subject': ['Math', 'English', 'Science', 'Arts'], 
    'TestScore': [89, 93, 91, 97]
}

classroom_df = pd.DataFrame(classroom_data)
print("\nClassroom DataFrame:\n", classroom_df)

classroom_df['ParticipationScore'] = [9, 10, 8, 10]
print("\n Updated DataFrame with 'ParticipationScore':\n", classroom_df)

teachers_data = {
    'Name': ['Sarah', 'Mike', 'Emma'],
    'Subject': ['English', 'Math', 'Science'],
}

teachers_df = pd.DataFrame(teachers_data)
print("Initial DataFrame:\n", teachers_df)

teachers_df['Years'] = [10, 5, 8]
print("\nDataFrame after a new column:\n", teachers_df)

teachers_df['Experience'] = [12, 6, 15]
print("\nDataFrame after adding 'Experience' column:\n", teachers_df)

# We have a list of classes and their respective teachers
classes_dict = {
    'Class': ['Math', 'Science', 'English', 'Physical Education'],
    'Teacher': ['Mr. James', 'Mrs. Smith', 'Ms. Williams', 'Mrs. Johnson']
}

# TODO: Create a DataFrame from the classes_dict
classes_df = pd.DataFrame(classes_dict)

# Display the DataFrame
print(classes_df)

# TODO: Create a dictionary named "classroom_data" with keys: StudentName, Subject, Grade. Assign corresponding values to these keys.
classroom_data = {
    'StudentName': ['Thiago', 'Amanda', 'Ágatha', 'Júlia', 'Lucas'],
    'Subject': ['Data Analytics', 'Instagram', 'Pedagogy', 'Math', 'English'],
    'Grade': ['5', '9', '6', '7', '3']
}

# TODO: Create a DataFrame named "classroom_df" using the "classroom_data" dictionary. Print it.
classroom_df = pd.DataFrame(classroom_data)
print(classroom_df)

# TODO: Add a new column 'AttendancePercentage' to the "classroom_df" DataFrame with values: 95, 80, 90, 85. Print the updated DataFrame.

classroom_df['AttendancePercentage'] = [95, 80, 90, 85, 75]
print(classroom_df)