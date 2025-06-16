FROM python:3.12-slim

WORKDIR /frontend

RUN mkdir -p /frontend/src

COPY ./src /frontend/src

COPY config.yml /frontend/

COPY requirements.txt /frontend/

RUN pip install -r requirements.txt

EXPOSE 8501 

CMD ["python", "-m", "streamlit", "run", "src/log-levels.py", "--server.address=0.0.0.0", "--server.port=8501"] 
