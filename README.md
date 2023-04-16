# 🐈 django-api
Backend REST API for my petcare management web app, petPal. Built with Django, originally part of devCodeCamp Capstone Project.

## Running locally

Create a virtual environment and install dependencies
```
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

### Normal setup
After cloning repo, use pipenv to create a virtual environment and install dependencies
```
cp .env.template .env
source .env
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
docker compose build
docker compose up -d
docker compose exec api python manage.py migrate
```

### Generate SSL Certs for HTTPS
SSH into the server running this API (after running `activate-ec2` script) and run:
```
sudo certbot --nginx
sudo systemctl restart nginx
```