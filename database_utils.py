import yaml
import psycopg2
from sqlalchemy import create_engine

 
#engine = create_engine("{type of database}+{DBAPI}://{username}:{password}@{host}:{port}/{database_name}")

class DatabaseConnector():                                  #Class name

        def __init__(self, yaml_file):   #init class + yaml file (data_utils) + attached data from yaml to class 
            self.yaml_file = yaml_file      #instance of args

        def read_db_creds(self):

            with open(self.yaml_file, 'r') as f:
            #('db_creds.yaml', 'r') as f:       # open db_creds.yaml file as f (format)
                data = yaml.safe_load(f)                # assigning yaml file as the variable data 

            #print(data)      # prints data of db creds                            
            return data        # returns data of db creds 

      
        def init_db_engine(self): 
            credentials = self.read_db_creds()    #credentials = reding the db creds file 
            #print(credentials)                      # prints creds
            return create_engine(f"{'postgresql'}+{'psycopg2'}://{credentials['RDS_USER']}:{credentials['RDS_PASSWORD']}@{credentials['RDS_HOST']}:{credentials['RDS_PORT']}/{credentials['RDS_DATABASE']}")
            # engine created - linked to credentials of db creds 

DB_Connector = DatabaseConnector('db_creds.yaml')  # created an instance that attached yaml file 
#print(DB_Connector.yaml_file[0:4]) # TEST to see if its connected to file - runs forst 4 charecters.
DB_Connector.read_db_creds()
DB_Connector.init_db_engine()
engine = DB_Connector.init_db_engine()
engine.connect()
