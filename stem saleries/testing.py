import pandas as pd

df = pd.read_csv(r"C:\Users\callu\Documents\PYTHON PROJECTS\pandas\stem saleries\STEM_saleries.csv") 

#converting the timestamp column to a datetime object
df['timestamp'] = pd.to_datetime(df['timestamp'])

print(df['title'].value_counts())