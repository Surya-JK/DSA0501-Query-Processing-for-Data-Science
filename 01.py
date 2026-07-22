import pandas as pd

# Load dataset
df = pd.read_csv('employees.csv')

# Get unique department IDs
distinct_dept = df['DEPARTMENT_ID'].unique()
print(distinct_dept)