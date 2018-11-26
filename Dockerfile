from python:3

COPY . /app
WORKDIR /app

RUN pip install -r requirements/dev.txt

EXPOSE 8000

CMD ls
CMD ["adev", "runserver"]
