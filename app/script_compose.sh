#!/bin/bash
docker-compose up -d
>&2 echo "Docker-compose runned, wait 4 second for running flask app"
sleep 4
>&2 echo "Flask app runned"
curl -X GET http://0.0.0.0:5000/add?file=test.json
>&2 echo "Test json file ready"
docker-compose stop
>&2 echo "Docker-compose stoped"
