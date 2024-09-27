# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY ./backend /app/backend
COPY ./fastapi_app /app/fastapi_app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "fastapi_app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
