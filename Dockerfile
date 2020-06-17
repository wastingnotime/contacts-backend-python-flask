FROM python:3.7.7-slim
WORKDIR /app
ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8010:8010


CMD ["python", "main.py"]