# Tuto Docker / Traefik
Simple Hello world with Python server / Docker / Traefik.
[Tuto create dev env with Docker and Traefik](https://medium.com/@fredericleaux/tuto-monter-un-environnement-de-dev-docker-avec-traefik-et-oauth2-pr%C3%AAt-pour-le-micro-service-12f78874d79c)

# Requirements :
- MS [Traefik-dockerize](https://github.com/restarteco/traefik-dockerized)

update your hosts:
- osx: `nano /etc/hosts`
- Linux (Debian based): `vim /etc/hosts`

and add : `127.0.0.1       local.second-service.fr`

# Run with docker
------------

```bash
docker-compose build
docker-compose up -d
```

the service run on port 5000