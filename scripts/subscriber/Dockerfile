# Subscriber/Dockerfile
FROM python:3.8

WORKDIR /app

COPY ../../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./scripts/subscriber/subscriber.py .
COPY ./scripts/constants.py .
COPY ./scripts/connect connect
COPY ./scripts/print_mongo.py .
COPY ./scripts/redis_test.py .

CMD ["python", "subscriber.py"]

