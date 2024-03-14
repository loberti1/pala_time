from sqlalchemy import create_engine,text

#generate connection
server = 'E-01520'
database = 'glob_dw'
username = 'sqlserverluciano'
password = 'crisiscore789'
connection = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(connection)

#sql query
try:
    with engine.connect() as my_connection:
        sql = text("SELECT 1")
        execute_query = my_connection.execute(sql)
        print("connection working OK")
except Exception as e:
    print(f"error present: {e}")