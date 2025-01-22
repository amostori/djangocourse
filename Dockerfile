FROM python:3.13-bullseye
ENV PYTHONUNBUFFERED=1
RUN apt-get update 
RUN apt-get install -y gettext
RUN mkdir /code
WORKDIR /code
RUN pip install poetry==1.8.4
RUN poetry --version
COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY . .
RUN chmod 755 /code/start-django.sh
EXPOSE  8000
ENTRYPOINT ["/code/start-django.sh"]
