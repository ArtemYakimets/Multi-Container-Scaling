FROM python:3.9-slim-bullseye

RUN pip install flask numpy requests

WORKDIR /app

COPY aggregator.py /app

CMD python -u aggregator.py