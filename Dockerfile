from python:3.7.1-alpine3.8

WORKDIR /app
# optimize pip dependencies
ADD ./requirements /app/requirements
RUN pip install -r /app/requirements/dev.txt

COPY . /app

EXPOSE 8000

CMD ls
CMD ["adev", "runserver"]
