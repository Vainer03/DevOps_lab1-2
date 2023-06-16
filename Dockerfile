FROM python:3.10-slim
COPY ./ /app
ENTRYPOINT ["python", "main.py"]
