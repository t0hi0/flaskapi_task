#!/bin/bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data @test.json \
  http://localhost:5000/add
