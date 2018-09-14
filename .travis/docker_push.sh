#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build -t helloqiu95/mr.dc .
docker push helloqiu95/mr.dc