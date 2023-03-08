import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
from datetime import datetime

#importing the matplot functions from the pd_plt_funcs.py file
from pd_plt_funcs import av_role_saleries

#using the date range file to carry out anything date/timestamp related
from date_range import date_selection

#importing the dataframe
while True:
    df_input = input("please enter the filepath of the df: ")
    try:
        df = pd.read_csv(df_input)
        print("\nfound dataframe\n\nloading lots of things...")

        break
    except:
        print("\ncould not find dataframe, please make sure that you entered the correct filepath")

#making a menu function so that the user can select which data models to produce
def menu():
    options = input("""
    which data would you like to visualise?
    (1) Average Stem Role Saleries
    (x) stop the program
    please enter a corrosponding number: """)

    while True:
        if options == "x":
            print("""
            thankyou for using the pandas/matplotlib project!
            have a great day""")
            break

        elif options == "1":
            date_mask, str_start_date, str_end_date = date_selection()
            av_role_saleries(date_mask, str_start_date, str_end_date)
        
        else:
            print("not an option\nplease try again!\n")

menu()
