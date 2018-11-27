from python:3.7.1-alpine3.8

ARG requirements_file=dev.txt

WORKDIR /app
# optimize pip dependencies
ADD ./requirements /app/requirements
RUN pip install -r /app/requirements/$requirements_file

COPY . /app

EXPOSE 8000
