#import libraries
import pandas as pd
import os
from flask import Flask, request, send_file
from sqlalchemy import create_engine

#create application instance >> object class flask
app = Flask(__name__)

#generate connection - depends on your own
server = 'E-01520'
database = 'glob_dw'
username = 'sqlserverluciano'
password = 'crisiscore789'

connection = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(connection)

###LOAD DATA
#define Url and view function to apply, when a client sends a request to this route, this code
#would be applied as a response
@app.route('/load', methods = ['POST'])

def loading():
      
      """view function to load data to SQL Server tables"""

      #insert your own path, where your files are stored
      path = 'C:\\Users\\COREBI\\Desktop\\archivos\\'
      os.chdir(path)

      try:

        #loop to insert batches up to 1000 rows
        for file in ['jobs.csv', 'departments.csv', 'hired_employees.csv']:
            df = pd.read_csv(file, header = None, chunksize = 1000)
            for data in df:
                if file == 'jobs.csv':
                    data.columns = ['id_jobs','ds_jobs']
                elif file == 'departments.csv':
                    data.columns = ['id_departments','ds_departments']
                elif file == 'hired_employees.csv':
                    data.columns = ['id_custom_hired_employee','ds_hired_employee','id_datetime','id_departments','id_jobs']
                else: None

                data.to_sql(file.split('.')[0], engine, if_exists='append', index = False)

        return 'data was loaded successfully'
    
      except Exception as e:
        return f'error present: {e}'
      

###GENERATE 1st QUERY number_employees
@app.route('/firstquery', methods = ['GET'])

def quarterly_additions_query():

    """view function used to execute query needed for first requirement,\
        query is inside SQL folder"""
    
    try:

        #open and read the file containing sql query
        with open('C:\\Users\\COREBI\\Desktop\\repo\\game_master\\api_sql_server\\SQL\\dml_number_employees.sql', 'r') as x:
            sql_query = x.read()
        
        #create dataframe and save it as a csv, send it to however 
        #opens the browser in http://127.0.0.1:5000/firstquery
        df = pd.read_sql(sql_query, engine)
        df.to_csv('number_employees.csv', index = False)

        return send_file('number_employees.csv', as_attachment = True)
    
    except Exception as e:
        return f'error present: {e}'
    

###GENERATE 2nd QUERY hired_departments
@app.route('/secondquery', methods = ['GET'])

def hiring_above_mean():

    """view function used to execute query needed for second requirement,\
        query is inside SQL folder"""
    
    try:

        #open and read the file containing sql query
        with open('C:\\Users\\COREBI\\Desktop\\repo\\game_master\\api_sql_server\\SQL\\dml_hired_department.sql', 'r') as x:
            sql_query = x.read()
        
        #create dataframe and save it as a csv, send it to however 
        #opens the browser in http://127.0.0.1:5000/secondquery
        df = pd.read_sql(sql_query, engine)
        df.to_csv('hired_departments.csv', index = False)

        return send_file('hired_departments.csv', as_attachment = True)
    
    except Exception as e:
        return f'error present: {e}'

if __name__ == '__main__':
    app.run(debug=True)

#command to send requests for data loading:
#curl -X POST -F "jobs.csv=@C:\Users\COREBI\Desktop\archivos\jobs.csv" -F "departments.csv=@C:\Users\COREBI\Desktop\archivos\departments.csv" -F "hired_employees.csv=@C:\Users\COREBI\Desktop\archivos\hired_employees.csv" http://127.0.0.1:5000/load
