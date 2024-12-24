FROM python:3.9-slim-bullseye

RUN pip install Flask

WORKDIR /app

COPY consumer.py /app

CMD python -u consumer.py