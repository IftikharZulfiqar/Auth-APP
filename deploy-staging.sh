#!/bin/bash
#This script will pull the fresh code and 
#make fresh docker build for staging

git checkout $1
git pull
sudo docker build -t cheetay-auth .
sudo docker rm -f cheetay-auth
sudo docker run -dit -p 8000:80 --name cheetay-auth cheetay-auth:latest
