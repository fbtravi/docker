# Simple app in Flask

This app runs with three locations.

* /cache - > show time
* /nocache - > show time
* / -> "Hello Word"

In this aplication have exporter metrics from Prometheus at location /metrics.

## Functions of each file in this template

* docker-compose.yml -> create configs from run docker at docker compose
* app/app.py -> script python
* app/requirements.txt -> requeriments python from install in docker image
* app/Dockerfile -> create configs from run docker

* This template an example, for inspirantiom in your project.

## Network

This project is configured with network standard <fbtravi_net>, this
configuration serves to communicate all docker's of my other projects,
