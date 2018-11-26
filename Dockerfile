from python:3

# optimize pip dependencies
ADD requirements/dev.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8000

CMD ls
CMD ["adev", "runserver"]
