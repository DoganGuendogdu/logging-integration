# TODO: delete dir '/logging-integration'

FROM python:3.12-slim

WORKDIR /logging-integration

RUN mkdir -p /logging-integration/frontend/src

COPY ./src /frontend/src

COPY requirements.txt /frontend

COPY .env /frontend

RUN pip install -r /frontend/requirements.txt

EXPOSE 8501

CMD ["python", "-m", "streamlit", "run", "/frontend/src/App.py", "--server.address=0.0.0.0", "--server.port=8501"]
