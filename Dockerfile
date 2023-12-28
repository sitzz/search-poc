FROM python:3.11-alpine3.19

ARG REDIS_AUTH
ARG REDIS_HOST
ARG REDIS_PORT

ENV REDIS_AUTH=$REDIS_AUTH
ENV REDIS_HOST=$REDIS_HOST
ENV REDIS_PORT=$REDIS_PORT

WORKDIR /app

COPY requirements.txt requirements.txt
COPY ./src/ /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:8000", "--chdir", "/app"]
