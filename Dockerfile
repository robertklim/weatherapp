FROM python:3.6.5-slim-jessie
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/weatherapp/src
ADD src/requirements.txt /usr/src/weatherapp/src/
RUN pip install -r requirements.txt