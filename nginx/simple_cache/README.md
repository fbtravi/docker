# Simple cache Nginx

This Nginx have three locations:

* /cache - > Nginx preserver cache per 5m
* /nocache - > Nginx not preserver cache
* / -> Nginx not preserver cache

These locations send requests to an simple_app_flask, which is in
[this projects](https://github.com/fbtravi/docker).
Just start before this app.

## For run linux

* This requerid docker running in SO
* Instaled docker compose

```bash
docker-compose up --build
```

```bash
location / {
            proxy_pass http://ups_my_app;
        }
        location /nocache {
            proxy_pass http://ups_my_app/nocache;
        }
        location /cache {
            proxy_cache mycache;
            proxy_cache_valid any 5m;
            proxy_pass http://ups_my_app/cache;
        }
```

## Testings

## Functions of each file in this template

* docker-compose.yml -> create configs form run docker at docker compose
* nginx/nginx.conf -> configuration of nginx

* This template an example, for inspirantiom in your project.

## Network

This project is configured with network standard <fbtravi_net>, this
configuration serves to communicate all docker's of my other projects.
