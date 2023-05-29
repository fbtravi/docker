# Prometheus simple config

## For run linux

* This requerid docker running in SO
* Instaled docker compose

```bash
docker-compose up --build
```

## Testings

In your browser assesing:

<http://localhost:9090> open interface the Prometheus

## Functions of each file in this template

* docker-compose.yml -> create configs form run docker at docker compose
  * networks -> using to conect another docker project
* mount_point -> mount_point for prometheus using
* mount_point/prometheus.yml -> configuration of prometheus

* This template an example, for inspirantiom in your project.
