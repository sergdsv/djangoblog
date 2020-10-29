FROM python:3.7

ENV PYTHONUNBUFFERED 0

COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt
