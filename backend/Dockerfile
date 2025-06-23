FROM python:3.12-slim

WORKDIR /backend

RUN mkdir -p /backend/src

COPY ./src /backend/src

COPY requirements.txt /backend//

RUN pip install -r requirements.txt

EXPOSE 1111

CMD ["uvicorn", "src.main:app", "--log-level", "debug", "--host", "0.0.0.0",  "--port", "1111"]