#!/bin/bash
docker run -d -p 5000:5000 flaskapi_task
>&2 echo "Docker container flaskapi_task runned, wait 4 second for running flask app"
sleep 4
>&2 echo "Flask app runned"
curl -X GET http://0.0.0.0:5000/add?file=test.json
>&2 echo "Test json file ready"
docker stop $(docker ps -q --filter ancestor=flaskapi_task )
>&2 echo "Docker container flaskapi_task stoped"
