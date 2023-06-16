FROM python:3.10-slim
WORKDIR calculator
COPY ./ /app
RUN apk update && pip install -r /app/requirements.txt --no-cache-dir
RUN pip install -e /app
EXPOSE 8080
ENTRYPOINT ["python", "main.py"]
