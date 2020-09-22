#!/bin/bash

docker-compose down
docker-compose -p reportportal up -d --force-recreate