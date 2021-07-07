FROM python:3.8.5

RUN pip install --upgrade pip

WORKDIR /pis_code

ENV FLASK_APP main.py

ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run"]