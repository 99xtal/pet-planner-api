# 🐈 pet-planner-api
Backend REST API for my petcare management application, petPal. Built with Django, Part of devCodeCamp Capstone Project.

## Running locally

There are two ways to set up this project locally. The first way is to only launch the Django server with DB envvars set locally. The better way is to spin up a development environment with Docker Compose.

### Normal setup
After cloning repo, use pipenv to create a virtual environment and install dependencies
```
cp .env.template ./api/.env
source .env
pipenv install
```
Run migrations if necessary, and run the app
```
(venv) python manage.py migrate
(venv) python manage.py runserver
```

### Docker setup
Running locally the Docker way is preferred because it is closer to how the application behaves in a production environment. The docker compose dev environment has 3 containers:
- `nginx`: Reverse proxy and static file server for Django web app
- `api`: The Django web application
- `db`: A MySql instance that the web app connects to.

***Setup Commands***
```
docker compose -f docker-compose.dev.yml build
docker compose -f docker-compose.dev.yml up -d
docker compose exec api python manage.py migrate

```
