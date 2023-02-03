FROM python:3.11

WORKDIR /app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

ENV PYTHONUNBUFFERED=1

RUN pip install pipenv
RUN pipenv install --system --deploy

COPY . .

ENTRYPOINT [ "python3" ]
CMD ["manage.py", "runserver", "0.0.0.0:8000"] 