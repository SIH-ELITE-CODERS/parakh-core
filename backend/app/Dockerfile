FROM python:3.8.5

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./start.sh /code/start.sh

COPY ./core /code/core
