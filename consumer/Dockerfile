FROM python:3.9-slim-bullseye

RUN apt-get update && apt-get install -y curl

RUN pip install Flask

WORKDIR /app

COPY consumer.py /app

CMD python -u consumer.py