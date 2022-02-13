FROM python:3.8-alpine
WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

EXPOSE 8010:8010

VOLUME data

ENV DB_LOCATION=/data/contacts.db
ENV FLASK_ENV=production

CMD ["python", "main.py"]