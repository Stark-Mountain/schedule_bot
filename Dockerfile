from python:3.7.1-alpine3.8

# optimize pip dependencies
ADD requirements/dev.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8000

CMD ls
CMD ["adev", "runserver"]
