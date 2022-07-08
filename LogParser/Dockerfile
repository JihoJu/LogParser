FROM python:3.8.11

WORKDIR /code/LogParser

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY * .