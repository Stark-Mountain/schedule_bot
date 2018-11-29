from python:3.7.1-alpine3.8

# aiopg requires psycopg2, but not psycopg2-binary, so we need to build it ourself
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install psycopg2 \
  && apk del build-deps

ARG requirements_file=dev.txt

WORKDIR /app
# optimize pip dependencies
# FIXME such optimization ignore new pip dependencies and requires
# container prune
ADD ./requirements /app/requirements
RUN pip install -r /app/requirements/$requirements_file

COPY . /app

EXPOSE 8000
