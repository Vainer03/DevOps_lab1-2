FROM python:3.10-slim
WORKDIR calculator
COPY main.py main.py
ENTRYPOINT ["python", "main.py"]
