# docker_demo
creating docker network and container 
# Docker Apache Networking Demo

Ten projekt pokazuje, jak skonfigurować sieć Dockerową oraz uruchomić dwa kontenery: serwer Apache i klienta, który łączy się z serwerem.

## Wymagania

- Docker
- Docker Compose

## Uruchomienie projektu

1. Sklonuj to repozytorium:

   ```bash
   git clone https://github.com/MaksymilianKnyba/docker-demo.git
   cd docker-demo
   docker-compose up --build
## http://localhost:8080
   docker logs client
