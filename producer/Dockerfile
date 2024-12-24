FROM python:3.9-slim-bullseye

RUN pip install requests

WORKDIR /app

COPY producer.py /app

CMD python -u producer.py