FROM python:3.12-slim

WORKDIR /backend

RUN mkdir -p /backend/src

RUN mkdir -p /backend/bin

RUN mkdir -p /backend/config

COPY ./src /backend/src

COPY ./bin /backend/bin

COPY ./config /backend/config

COPY requirements.txt /backend

COPY .env /backend/

RUN apt-get update

RUN apt-get install jq -y

RUN apt-get install gettext -y

RUN pip install -r requirements.txt

EXPOSE 1111

CMD ["uvicorn", "src.main:app", "--log-level", "debug", "--host", "0.0.0.0",  "--port", "1111"]
