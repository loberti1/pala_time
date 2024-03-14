#I'm using current python runtime in this repo
FROM python:3.8.2-slim
#working directory to the container
WORKDIR /app

#copy requirements.txt with the needed libraries, contents in directory and sql files
COPY requirements.txt .
COPY . /app
COPY SQL /app/SQL

#install needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

#flask port and run command defined
EXPOSE 80
CMD ["python", "app_api_glob.py"]
#end