#this file contains all functions which are date related so that they can be resused infinetly if 
#it was neccarsary, the point is that having everything date related organised in functions in a seperate file
#means that this projects code is more efficient, tidy, understandable easier to maintain and
#all of this code can even be reused by other projects, saving time. 

import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
from datetime import datetime
import re

from df_reader import dffunc
df = dffunc()


#this is an oop file i made with functions to grab the earliest and also the latest datetimes in a pd sereies
class date_functions:
    # creating the initialiser
    def __init__(self, date_column):
        try:
            import pandas as pd
        except:
            print('pandas is not installed, please run pip install pandas in the terminal')
        self._date_column_nformat = date_column
        self._date_column = pd.to_datetime(
        self._date_column_nformat, dayfirst=False)

    # this function grabs the earliest date in a series
    def min_date(self):
        self._min_date = self._date_column.min()
        min_date_ = pd.to_datetime(self._min_date, dayfirst=False)
        return min_date_

    # this function grabs the latest date in a series
    def max_date(self):
        self._max_date = self._date_column.max()
        max_date_ = pd.to_datetime(self._max_date, dayfirst=False)
        return max_date_


#converting the timestamp column to a datetime object
df['timestamp'] = pd.to_datetime(df['timestamp'])

dates = date_functions(df["timestamp"])

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

def date_selection():
    flag=True
    while flag == True:
        all_dates = input("enter A to show all salaries for all dates or S to select a daterange: ").upper()
        try:    
            if all_dates == "S":
                start_date = get_start_date()
                end_date = get_end_date()

                if start_date<dates.min_date() or end_date>dates.max_date():
                    print("\ndate(s) out of range, please try again")
                    start_date = get_start_date()
                    end_date = get_end_date() 
                flag=False

            elif all_dates == "A":
                start_date = dates.min_date()
                end_date = dates.max_date()
                flag=False
            
            else:
                print("Sorry thats not an option, please try again\n")

            #creating the datemask
            date_mask = df.loc[(df["timestamp"] >= start_date) & (df["timestamp"] <= end_date)].copy()

            #converting dates to date strings rather than timestamps so we van use them in the plt title 
            str_start_date = datetime.strftime(start_date, "%Y-%m-%d")
            str_end_date = datetime.strftime(end_date, "%Y-%m-%d")

            return date_mask, str_start_date, str_end_date
        except:
            print("error getting start and end date")

def date_select_again():
    while True:
        more = input("""
        would you like to select another daterange to compare?
        please enter yes or no: """)
        more.lower()

        #using regex to clean up the users input and make sure 
        # that there is at least one word there before we proccess anything else
        try:
            more = re.search(r'[a-z]{2,9}', more).group()
        except:
            print("not gonna work!\n")
            continue
        
        if more=="yes" or more=="yeah" or more=="please" or more=="indeed":
            return True
        elif more=="no" or more=="nah" or more=="nay":
            return False
