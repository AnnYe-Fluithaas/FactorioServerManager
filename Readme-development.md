This readme is intended for those who develop this application, not for use of the application itself.

# Pre-requisites 
* Docker installed

# Running the project

* Load up docker.  
* In commandline: `docker-compose up --build`  
* Wait a bit  
* When ready, the application will be available at http://localhost:8000/  

## Dev tools
A second Docker Compose file is added that allows browsing the data in redis and postgres. To execute, run in the commandline:
* `docker-compose -f .\compose-dev.yaml up -d --build`
* `docker-compose up --build`

You can browse the **postgres** database via pgAdmin by connecting to `http://localhost:8082`

You can test our the **GraphQL** queries by connection to `http://localhost:8080/graphql`

## Development Architecture
* Frontend application: **Javascript React**  
* Backend application: **Python Django**
* Communication between frontend and backend: **GraphQL** (Using Graphene library in Django, Apollo Client in React)
* Database: **Postgres SQL** and **Redis**

### Folder structure
**FactorioServerManager** -- The main Django project. Includes overall settings.  
**calendars** -- supporting Django app. Handles calendars.  
**frontend** -- React app. Handles the frontend and .html pages.  
**games** -- supporting Django app.  
**servers** -- supporting Django app.  
