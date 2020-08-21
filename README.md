# Flask API test task

This test project contains API for get json file with numbers and return sum of numbers as json

## Development

Clone the repo from GitHub using:
> git clone https://github.com/t0hi0/flaskapi_task.git

Create a Python3 virtual env and activate:
> python3 -m venv /path/to/venv

> path/to/venv$ Scripts/activate.bat

Go to 'app' directory. Install required packages:
> (virtualenv)path/to/flaskapi_task/app$ pip install -r requirements.txt

Running the project:
> (virtualenv)path/to/flaskapi_task/app$ python3 app.py

## Deployment

Deploy the API using the Docker compose from 'app' directory:
> path/to/flaskapi_task/app$ docker-compose up

## Test
After build Dockerfile you can test API with script.sh in main directory. 
Make the script executable: 
> path/to/flaskapi_task$ chmod +x script.sh

And run:
> path/to/flaskapi_task$ ./script.sh

This script send test.json from main directory to API. You can replace script.sh and test json to any place and 
run script. For send other json to API edit json file name in script (--data @test.json). 
Also you can use json-format in curl:
> curl --header "Content-Type: application/json" --request POST
> --data '{"numbers": [1,2,3,4]}' http://localhost:5000/add