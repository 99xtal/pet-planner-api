FROM python:3.11

WORKDIR /app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

ENV PYTHONUNBUFFERED 1
ENV APP_HOME /home/app/api

RUN mkdir ./staticfiles

RUN pip install pipenv
RUN pipenv install --system --deploy

COPY . .
RUN python3 manage.py collectstatic

ENTRYPOINT [ "gunicorn" ]
CMD ["-b", "0.0.0.0:8000", "pet_planner_project.wsgi:application"] 