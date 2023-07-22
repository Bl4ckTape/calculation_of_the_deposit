FROM python:3.10-slim

RUN pip install pipenv

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY Pipfile Pipfile.lock .
RUN pipenv install --system --ignore-pipfile

COPY . /app
COPY /app /app
ENTRYPOINT ["python"]
CMD ["main.py"]