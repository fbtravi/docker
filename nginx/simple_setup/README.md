# Nginx simple config

## For run linux

* This requerid docker running in SO
* Instaled docker compose
```
docker-compose up --build
```

## Testings

In your browser assesing:

http://localhost:8080/index.html this url must return `WORKING`

http://localhost:8080/pudim this url will redirect to http://www.pudim.com.br


## Functions of each file in this template

* docker-compose.yml -> create configs form run docker at docker compose
* index.html -> htlm page to display
* nginx.conf -> configuration of nginx

* This template an example, for inspirantiom in your project.