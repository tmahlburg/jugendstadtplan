# python3 container using alpine linux
# initial source: https://docs.docker.com/compose/django/

FROM python:3-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
RUN apk add zlib-dev jpeg-dev gcc musl-dev
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
