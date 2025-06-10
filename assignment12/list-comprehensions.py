import pandas as pd

# CSV
df = pd.read_csv("../csv/employees.csv")

# Task 3.1: 
full_names = [row['first_name'] + " " + row['last_name'] for index, row in df.iterrows()]
print("All full names:")
print(full_names)

# Task 3.2:
names_with_e = [name for name in full_names if 'e' in name.lower()]
print("\nNames with 'e':")
print(names_with_e)
