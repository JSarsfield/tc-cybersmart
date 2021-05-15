# syntax=docker/dockerfile:1
FROM python:3.9.5-buster as base
ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt
COPY . /src/

CMD python manage.py runserver 0.0.0.0:8080