FROM python:3.10-slim
WORKDIR calculator
COPY ./ /app
ENTRYPOINT ["python", "main.py"]
