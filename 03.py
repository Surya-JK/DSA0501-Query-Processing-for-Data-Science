import pandas as pd

df = pd.read_csv('jobs.csv')

# Sort by JOB_TITLE descending
sorted_jobs = df.sort_values(by='JOB_TITLE', ascending=False)
print(sorted_jobs)