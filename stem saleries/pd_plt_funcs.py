# this file holds all the matplot lib and pandas functions to plot the graphs based on pandas 
# masks and filters. these functions are called in the menu in main.py


import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
from datetime import datetime

def av_role_saleries(_date_mask, _str_start_date, _str_end_date):
    # getting the saleries for each role into a new list called sals
    roles = ['Software Engineer', 'Product Manager', 'Software Engineering Manager', 'Data Scientist', 'Hardware Engineer', 'Product Designer', 'Technical Program Manager']
    sals = []
    for role in roles:
        sals.append(_date_mask.loc[_date_mask['title'] == role]['totalyearlycompensation'].mean().__round__(0))

    #plotting data into a bar graph using the matplotlib module
    plt.figure(figsize=(6,3)).set_tight_layout(tight=True)
    plt.style.use('ggplot')
    plt.xticks(fontsize = 7)
    plt.xticks(rotation = -17, ha='left')
    plt.xticks()
    plt.title(f'STEM Role Saleries from {_str_start_date} to {_str_end_date}')
    plt.xlabel('Roles')
    plt.ylabel('Saleries ($)')
    plt.bar(roles, sals, align='center', width=0.5)
    plt.show(block=False)


def gender_ratio(_date_mask, _str_start_date, _str_end_date):
    male = int((_date_mask['gender'].loc[_date_mask['gender']=='Male']).value_counts())
    female = int((_date_mask['gender'].loc[_date_mask['gender']=='Female']).value_counts())

    plt.figure(figsize=(6,3)).set_tight_layout(tight=True)
    plt.style.use('ggplot')
    plt.title(f'STEM Role Gender Ratio from {_str_start_date} to {_str_end_date}')
    plt.pie([male, female], labels=['Male', 'Female'], colors=["#6fa8dc", "#ff80b1"])
    plt.show(block=False)

# TODO make more matplotlib functions and then add it in the main menu
