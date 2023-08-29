# Publisher/Dockerfile
FROM python:3.8

WORKDIR /app

COPY ../../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./scripts/publisher/publisher.py .
COPY ./scripts/connect connect
COPY ./scripts/constants.py .
COPY ./scripts/req.py .

CMD ["python", "publisher.py"]

