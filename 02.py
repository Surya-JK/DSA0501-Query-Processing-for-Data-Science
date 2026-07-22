import pandas as pd

df = pd.read_csv('job_history.csv')

# Count occurrences of employee IDs and filter
job_counts = df['EMPLOYEE_ID'].value_counts()
employees_with_multiple_jobs = job_counts[job_counts >= 2].index.tolist()

print("Employee IDs with two or more past jobs:", employees_with_multiple_jobs)