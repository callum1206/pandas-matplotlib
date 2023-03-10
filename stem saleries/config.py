#this file checks that all required modules are installed.
#the function is called in main before anything trys being proccessed

def module_import():
    error_string = "error importing {0}\nplease run 'pip install {0} in the terminal'"
    try:
        import pandas as pd
    except:
        print(error_string.format("pandas"))
    try:
        import matplotlib as mpl
        from matplotlib import pyplot as plt
    except:
        print(error_string.format("matplotlib"))
    try:
        from datetime import datetime
    except:
        print(error_string.format("datetime"))
    try:
        import re
    except:
        print(error_string.format("re"))