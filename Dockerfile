FROM python:3.7.7-slim
WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

EXPOSE 8010:8010

ENV FLASK_ENV=production

CMD ["python", "main.py"]