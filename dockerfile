FROM python:3.12.4-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE ${API_PORT}
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${API_PORT}"]
