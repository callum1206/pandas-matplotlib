from config import module_import

module_import()

file_import_error = """
error importing the {0} file into main
please make sure all files are in the same directory and have unchanged file names"""
#importing the matplot functions from the pd_plt_funcs.py file
try:
    from pd_plt_funcs import av_role_saleries, gender_ratio
except:
    print(file_import_error.format("pd_plt_funcs.py"))

#using the date range file to carry out anything date/timestamp related
try:
    from date_funcs import date_selection, date_select_again
except:
    print(file_import_error.format("date_funcs.py"))


#making a menu function so that the user can select which data models to produce
def menu():
    while True:
        options = input("""
        which data would you like to visualise?
        (1) Average Stem Role Saleries
        (2) Gender Ratio in Stem Roles
        (x) stop the program
        please enter a corrosponding number: """)


        if options == "x":
            print("""
            thankyou for using the pandas/matplotlib project!
            have a great day""")
            break

        elif options == "1":
            while True:
                date_mask, str_start_date, str_end_date = date_selection()
                av_role_saleries(date_mask, str_start_date, str_end_date)

                repeat = date_select_again()
                if repeat == True:
                    continue
                else:
                    print("no worries\n")
                    break

        elif options == "2":
            while True:
                date_mask, str_start_date, str_end_date = date_selection()
                gender_ratio(date_mask, str_start_date, str_end_date)

                repeat = date_select_again()
                if repeat == True:
                    continue
                else:
                    print("no worries\n")
                    break

        else:
            print("not an option\nplease try again!\n")

menu()
