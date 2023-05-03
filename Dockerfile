FROM python:2.7.18-buster

WORKDIR /app

ADD requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

ADD test.py /app

CMD [ "python", "/app/test.py" ]
