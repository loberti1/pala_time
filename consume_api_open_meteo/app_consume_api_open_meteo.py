"""Code to get data from open meteo and define a fault tolerant and scalable pipeline"""
import pandas as pd, requests as re, datetime, timedelta, pyodbc

#generate connection - depends on your own
connection_str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=E-01520;DATABASE=OpenMeteo;UID=sqlserverluciano;PWD=crisiscore789"
connection = pyodbc.connect(connection_str)
cursor = connection.cursor()

#truncate staging table
with open('C:\\Users\\Luciano\\Desktop\\git\\pala_time\\consume_api_open_meteo\\SQL\\dml_truncate_stg.sql') as query:
    sql_query = query.read()
cursor.execute(sql_query)
connection.commit()

#location Buenos Aires and time range for pipeline
latitude = -34.603722
longitude = -58.381592
end_date = datetime.datetime.today().date()
start_date = end_date - timedelta.Timedelta(days = 7)

#url api - get data
url = f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&hourly=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m"
response = re.get(url)
data = response.json()

#generate dataframe and conversions
df = pd.DataFrame({
    "timestamp": data["hourly"]["time"],
    "temperature_2m": data["hourly"]["temperature_2m"],
    "relative_humidity_2m": data["hourly"]["relative_humidity_2m"],
    "precipitation": data["hourly"]["precipitation"],
    "wind_speed_10m": data["hourly"]["wind_speed_10m"],
})

df["timestamp"] = pd.to_datetime(df["timestamp"])

#insert data
df.to_sql('stg_openmeteo',connection,'dbo', if_exists='append')

#use merge to insert when matched and update when not matched
with open('C:\\Users\\Luciano\\Desktop\\git\\pala_time\\consume_api_open_meteo\\SQL\\dml_truncate_stg.sql') as query:
    sql_query = query.read()
cursor.execute(sql_query)
connection.commit()