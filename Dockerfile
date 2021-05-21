FROM python:3.7-alpine
#MAINTAINER Murlai Krishna First Application

ENV PYTHONUNBUFFERED 1

COPY ./requiremetns.txt /requiremetns.txt
RUN pip install -r /requiremetns.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
