FROM python:3.8.5

RUN pip install --upgrade pip

WORKDIR /neuronnetwork

ENV FLASK_APP manage.py

ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run"]