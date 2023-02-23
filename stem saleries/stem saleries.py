import pandas as pd
import copy
import datetime
from datetime import datetime
import matplotlib as mpl
from matplotlib import pyplot as plt

df = pd.read_csv(r"C:\Users\callu\Documents\PYTHON PROJECTS\pandas projects\stem saleries\STEM_saleries.csv") 

#converting the timestamp column to a datetime object
df['timestamp'] = pd.to_datetime(df['timestamp'])

#grabing the daterange
start_date = input("enter the start date in yyyy-mm-dd: ")
start_date = pd.to_datetime(start_date)


end_date = input("enter the end date in yyyy-mm-dd: ")
end_date = pd.to_datetime(end_date)

date_mask = df.loc[(df["timestamp"] >= start_date) & (df["timestamp"] <= end_date)].copy()

Software_Engineer_av_sal = (date_mask.loc[date_mask['title'] == 'Software Engineer']['totalyearlycompensation'].mean().__round__(0))
Product_Manager_av_sal = (date_mask.loc[date_mask['title'] == 'Product Manager']['totalyearlycompensation'].mean().__round__(0))
Software_Engineering_Manager = (date_mask.loc[date_mask['title'] == 'Software Engineering Manager']['totalyearlycompensation'].mean().__round__(0))
Data_Scientist = (date_mask.loc[date_mask['title'] == 'Data Scientist']['totalyearlycompensation'].mean().__round__(0))
Hardware_Engineer = (date_mask.loc[date_mask['title'] == 'Hardware Engineer']['totalyearlycompensation'].mean().__round__(0))
Product_Designer = (date_mask.loc[date_mask['title'] == 'Product Designer']['totalyearlycompensation'].mean().__round__(0))
Technical_Program_Manager = (date_mask.loc[date_mask['title'] == 'Technical Program Manager']['totalyearlycompensation'].mean().__round__(0))
Solution_Architect = (date_mask.loc[date_mask['title'] == 'Solution Architect']['totalyearlycompensation'].mean().__round__(0))
Management_Consultant = (date_mask.loc[date_mask['title'] == 'Management Consultant']['totalyearlycompensation'].mean().__round__(0))

sals = [Software_Engineer_av_sal, Product_Manager_av_sal, Software_Engineering_Manager, Data_Scientist, Hardware_Engineer, Product_Designer, Technical_Program_Manager]
roles = ['Software_Engineer_av_sal', 'Product_Manager_av_sal', 'Software_Engineering_Manager', 'Data_Scientist', 'Hardware_Engineer', 'Product_Designer', 'Technical_Program_Manager']

plt.figure(figsize=(11,6)).set_tight_layout(tight=True)
plt.style.use('ggplot')
plt.xticks(fontsize = 8)
plt.title(f'STEM Role Saleries from {start_date} to {end_date}')
plt.xlabel('Roles')
plt.ylabel('Saleries ($)')
plt.bar(roles, sals, align='edge', width=0.5)


plt.show()

