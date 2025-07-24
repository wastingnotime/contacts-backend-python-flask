# syntax=docker/dockerfile:1
FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# act as doc only
EXPOSE 8010
LABEL vendor=wastingnotime.org

VOLUME data

# default environment
ENV DB_LOCATION=/data/contacts.db
ENV FLASK_ENV=False

CMD ["python", "main.py"]