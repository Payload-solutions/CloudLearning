FROM python:3.8.5

COPY . .

WORKDIR /usr/app

RUN pip install --upgrade pip