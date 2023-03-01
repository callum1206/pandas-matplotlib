import pandas as pd
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


