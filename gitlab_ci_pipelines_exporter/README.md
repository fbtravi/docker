# Gitlab ci pipelines exporter simple config

## For run linux

* This requerid docker running in SO
* Instaled docker compose

```bash
docker-compose up --build
```

## Testings

In your browser assesing:

<http://localhost:8080/metrics> open metris this is exporter

## Functions of each file in this template

* docker-compose.yml -> create configs form run docker at docker compose
  * GCPE_GITLAB_TOKEN -> env var of gitlab token

* gitlab-ci-pipelines-exporter.yml -> config file from exporter

* This template an example, for inspirantiom in your project.

## Monitoring with Promtheus

For monitoring this container is it possible to use this project [Prometheus]
(<https://github.com/fbtravi/docker>)

Just add it at the end of the file prometheus.yml

```yaml
- job_name: gitlab_ci_exporter_exporter
  honor_timestamps: true
  scrape_interval: 15s
  scrape_timeout: 10s
  metrics_path: /metrics
  scheme: http
  static_configs:
  - targets:
    - gitlab_ci_pipelines:8080
```
