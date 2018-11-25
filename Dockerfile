from python:3

COPY . /app
WORKDIR /app

RUN pip install pipenv

RUN pipenv install --system --deploy

CMD ["adev", "runserver", "src/main.py"]
