# Observability simple setup

This project create one ecosistem at observability, includin Grafana, Prometheus
and node_exporter.

## For run linux

* This requerid docker running in SO
* Instaled docker compose

```bash
docker-compose up --build
```

## Testings

In your browser assesing:

* <http://localhost:3000> open interface the Grafana
* <http://localhost:9090> open interface the Prometheus
* <http://localhost:9100> open  metrics node_exporter
* <http://localhost:3000/d/rYdddlPWk/node-exporter-full> open dashboar
node_exporter

## Functions of each file in this template

* docker-compose.yml -> create configs form run docker at docker compose
  * In environment at Grafana have tags credentions at login
* This template an example, for inspirantiom in your project.
