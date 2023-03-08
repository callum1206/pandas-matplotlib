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
    plt.figure(figsize=(11,6)).set_tight_layout(tight=True)
    plt.style.use('ggplot')
    plt.xticks(fontsize = 8)
    plt.title(f'STEM Role Saleries from {_str_start_date} to {_str_end_date}')
    plt.xlabel('Roles')
    plt.ylabel('Saleries ($)')
    plt.bar(roles, sals, align='edge', width=0.5)
    plt.show()
