FROM python:3.10.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y

WORKDIR /src

COPY ./app /src/app
COPY ./main.py /src/main.py
COPY ./docker-entrypoint.sh /src/docker-entrypoint.sh
COPY ./pyproject.toml /src/pyproject.toml
COPY ./.env /src/.env

RUN apt update && \
    apt upgrade -y && \
    apt install -y ncat && \ 
    pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

RUN poetry install --only main

ENTRYPOINT [ "/src/docker-entrypoint.sh" ]
