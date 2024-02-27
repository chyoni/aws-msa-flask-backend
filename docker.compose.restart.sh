#!/bin/bash

docker stop flask-owner-service-backend

docker compose -f ./docker-compose.yml down

docker compose -f ./docker-compose.yml -p msa-owner-service up --build -d