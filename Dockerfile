FROM python:3.7.4

ENV PYTHONUNBUFFERED 1

RUN mkdir /todo
WORKDIR /todo
COPY requirements.txt /todo/


ENV PGDATA /etc/postgresql/11/main
ENV LOGDIR  /etc/postgresql/11/main/postgresql.log
RUN pip install -r requirements.txt

COPY . /todo/
