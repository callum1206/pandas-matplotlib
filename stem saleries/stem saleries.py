import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
from datetime import datetime

#this is an oop file i made with functions to grab the earliest and also the latest datetimes in a pd sereies
from oo_date_ranges import date_functions

#importing the dataframe
df = pd.read_csv(r"STEM_saleries.csv") 
#telling the date functions class what the date column is
dates = date_functions(df["timestamp"])

#converting the timestamp column to a datetime object
df['timestamp'] = pd.to_datetime(df['timestamp'])

#grabing the daterange
def get_start_date():
    flag = True
    while flag == True:
        date_input = input(f"""
the earliest date in the dataframe is {dates.min_date()}
the latest date in the dataframe is {dates.max_date()}
please enter the start date in yyyy-mm-dd format: """)
        try:
            strf_date = datetime.strptime(date_input, "%Y-%m-%d")
            pd_start_date = pd.to_datetime(strf_date)
            flag = False
            return pd_start_date
        except:
            flag = True
            print("sorry, looks like the date you entered is invalid\nplease make sure it is in the correct format\n")

def get_end_date():
    flag = True
    while flag == True:
        date_input = input(f"please enter the end date in yyyy-mm-dd format: ")
        try:
            strf_date = datetime.strptime(date_input, "%Y-%m-%d")
            pd_end_date = pd.to_datetime(strf_date)
            flag = False
            return pd_end_date
        except:
            flag = True
            print("sorry, looks like the date you entered is invalid\nplease make sure it is in the correct format\n")

start_date = get_start_date()
end_date = get_end_date()

#creating the datemask
date_mask = df.loc[(df["timestamp"] >= start_date) & (df["timestamp"] <= end_date)].copy()

# getting the saleries for each role into a new list called sals
roles = ['Software Engineer', 'Product Manager', 'Software Engineering Manager', 'Data Scientist', 'Hardware Engineer', 'Product Designer', 'Technical Program Manager']
sals = []
for role in roles:
    sals.append(date_mask.loc[date_mask['title'] == role]['totalyearlycompensation'].mean().__round__(0))

#plotting data into a bar graph using the matplotlib module
plt.figure(figsize=(11,6)).set_tight_layout(tight=True)
plt.style.use('ggplot')
plt.xticks(fontsize = 8)
plt.title(f'STEM Role Saleries from {start_date} to {end_date}')
plt.xlabel('Roles')
plt.ylabel('Saleries ($)')
plt.bar(roles, sals, align='edge', width=0.5)
plt.show()


