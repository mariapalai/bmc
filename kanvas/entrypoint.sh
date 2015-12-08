#!/bin/sh
#
# Script to run either locally on a machine with django 1.8.5 in virtualenv or to deploy a dockerized version
# Note that each 'docker run' command is isolated
#
# Usage:
# For development (note the dot in the beginning): . ./entrypoint.sh virtualenv [path to file 'activate']
# For deployment: ./entrypoint.sh build && ./entrypoint.sh deploy

start() {
    python2.7 manage.py makemigrations
    python2.7 manage.py migrate
    python2.7 manage.py runserver 0.0.0.0:8085         # accessible to network, not only to localhost:8085
}

if [ $# -eq 0 ]; then                               # if there is no argument
    start
elif [ "$1" = "virtualenv" ]; then                  # else there is at least one argument
    source $2
    start
elif [ "$1" = "build" ]; then
    docker build --tag="kanvas/django:v1.8.5" --rm=true .
elif [ "$1" = "deploy" ]; then                      # creates docker container and runs first if clause from the container
    docker run -p 8085:8085 -ti kanvas/django:v1.8.5
elif [ "$1" = "ssh" ]; then                         # only for troubleshooting
    docker run -p 8085:8085 -ti kanvas/django:v1.8.5 /bin/bash
fi
