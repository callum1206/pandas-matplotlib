import pandas as pd

# this functions has a couple trys of automatically finding the dataframe
# before eventually asking the user to enter the file path
# which means it could save the user hassle and time, it also means that errors can be caught 
# so there is always a dtaframe returned before anything else can run

def import_df():
    print("looking for stem saleries dataframe\n")
    try:
        _df=pd.read_csv('STEM_Saleries.csv')
        return _df
    except:
        try:
            _df=pd.read_csv('STEM_saleries.csv')
            return _df
        except:
            print("we couldnt find it :( ")
            while True:
                df_input = input("please enter the filepath of the df: ")
                try:
                    _df = pd.read_csv(df_input)
                    print("\nthank you\n\nloading lots of things...")

                    return _df
                except:
                    print("\ncould not find dataframe, please make sure that you entered the correct filepath")

# this is a very simple function witch uses the other one to grab the df
#this is what we call into other files. its called the date functions file
def dffunc():
    _df = import_df()
    return _df

