
from database_utils import DatabaseConnector
from sqlalchemy import inspect             # listing table from sql alcemy engine - google search      
import pandas as pd


class DataExtractor():
    def __init__ (self, engine):            # initlisation class 
        self.inspector = inspect(engine)        # creating an attribute inspecto using the inspect method on the already created engine 
        self.engine = engine.connect()

    
    def list_db_tables(self):
            return self.inspector.get_table_names()
            
    def read_rds_table(self, table):      # reading tables from sqlalchemy engine google search
        df = pd.read_sql_table(table, self.engine)
        return df
    

DB_Connector = DatabaseConnector('db_creds.yaml')  #Binding method list_db_tables to DB_Connector 
DB_Extractor = DataExtractor(DB_Connector.init_db_engine())   # DB_connector is the instance of the engine class
DB_Extractor.list_db_tables()

df_legacy_store_details = DB_Extractor.read_rds_table('legacy_store_details')
df_legacy_users = DB_Extractor.read_rds_table('legacy_users')
df_orders_table = DB_Extractor.read_rds_table('orders_table')

    
    

        


