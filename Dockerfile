FROM python:3.10-slim
WORKDIR app
COPY main.py main.py
ENTRYPOINT ["python", "main.py"]
