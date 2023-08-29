# FastAPI/Dockerfile
FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./scripts/fastapi/main.py .
COPY ./scripts/connect connect
COPY ./scripts/constants.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

