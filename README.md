# docker_demo
creating docker network and container 
# Docker Apache Networking Demo

Ten projekt pokazuje, jak skonfigurować sieć Dockerową oraz uruchomić dwa kontenery: serwer Apache i klienta, który łączy się z serwerem.

## Wymagania

- Docker
- Docker Compose
- python
- flask

## Uruchomienie projektu

1. Sklonuj to repozytorium:

   ```bash
   git clone https://github.com/MaksymilianKnyba/listazadan.git
   cd docker-demo
   docker-compose up --build
## http://localhost:5000
   strona z listą zadan
## http://localhost:8081 
   serwer apache
## http://localhost:3000
   grafan
## http://localhost:9090
   prometheus
# lista zadan
