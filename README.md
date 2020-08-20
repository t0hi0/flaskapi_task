# Flask API test task

This test project contains API for get json file with numbers and return sum of numbers as json

## Development

Clone the repo from GitHub using
> git clone https://github.com/t0hi0/flaskapi_task.git

Create a Python3 virtual env and activate
> python3 -m venv /path/to/venv
> path/to/venv$ Scripts/activate.bat

Go to 'app' directory. Install required packages
> (virtualenv)path/to/flaskapi_task/app$ pip install -r requirements.txt

Running the project
> (virtualenv)path/to/flaskapi_task/app$ python3 app.py

Performing sum a json file '{"numbers": [1,2,3,4]}':
> curl -X GET http://0.0.0.0:5000/add?file=/full/path/to/file.json

## Deployment
Deploy the API using the Dockerfile within this project

> path/to/flaskapi_task/app$ docker build -t flaskapi_task .
> path/to/flaskapi_task/app$ docker run -d -p 5000:5000 flaskapi_task

Deploy the API using the Docker compose 
> path/to/flaskapi_task/app$ docker-compose up

## Test
After build Dockerfile you can test API (test.json) with script.sh in main directory. Grant privileges for script and run: 
> path/to/flaskapi_task$ chmod +x script.sh
> path/to/flaskapi_task$ ./script.sh

Also you can test API (test.json) with script_compose.sh in 'app' directory. Grant privileges for script and run: 
> path/to/flaskapi_task/app$ chmod +x script_compose.sh
> path/to/flaskapi_task/app$ ./script_compose.sh