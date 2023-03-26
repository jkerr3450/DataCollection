import pandas as pd
from data_extraction import df_legacy_users # legacy user df passed in 
from data_extraction import df_legacy_store_details
from data_extraction import df_orders_table



class DataCleaning():
    def __init__(self, df):   # legacy users df passed in
        self.df = df
         

    def clean_user_data(self):
        self.df.dropna(inplace = True, axis = 1)   # drops null values, inplace carries out action inplace, axies starts at 1 colum(2)

        return self.df

        
print(df_legacy_users.isnull().sum())   # tells how many null values are in each column 
print(df_legacy_store_details.isnull().sum()) 
print(df_orders_table.isnull().sum()) 


cleaner_1 = DataCleaning(df_legacy_users)   # instance of the class with data frame 
cleaner_2 = DataCleaning(df_legacy_store_details)
cleaner_3 = DataCleaning(df_orders_table)

df_legacy_users_clean = cleaner_1.clean_user_data()   # creating a clean cleaner_1 
df_legacy_store_details_clean = cleaner_2.clean_user_data()
df_orders_table_clean = cleaner_3.clean_user_data()

print(df_legacy_users_clean.isnull().sum())   # printing number of null values in the cleaned df + checking for removed features 
print(df_legacy_store_details_clean.isnull().sum()) 
print(df_orders_table_clean.isnull().sum()) 


#Step 6:
#You will need clean the user data, look out for NULL values, errors with dates, 
#incorrectly typed values and rows filled with the wrong information.


## need to clean date errors, + incorrectly typed values and rows filled with the wrong information.

