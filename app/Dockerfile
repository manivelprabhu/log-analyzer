FROM python:3.12-slim

WORKDIR /app

COPY app.py .
COPY sample.log .

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
