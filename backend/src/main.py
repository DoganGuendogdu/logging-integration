from fastapi  import FastAPI
from pydantic import BaseModel
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response


log_counter = Counter("log_events_total", "Counts number of entries for every log level", ["level"])

class Message(BaseModel):
    info_message:str

app = FastAPI()

@app.post("/log/info")
async def log_endpoint_info(info_message:Message):
    log_counter.labels(level="INFO").inc()
    return {"message": f"severity with log level 'INFO' and content: {info_message}"} 

@app.post("/log/debug")
async def log_endpoint_info(debug_message:Message):
    log_counter.labels(level="DEBUG").inc()
    return {"message": f"severity with log level 'DEBUG' and content: {debug_message}"} 

@app.post("/log/warning")
async def log_endpoint_info(warning_message:Message):
    log_counter.labels(level="WARNING").inc()
    return {"message": f"severity with log level 'WARNING' and content: {warning_message}"} 

@app.post("/log/error")
async def log_endpoint_info(error_message:Message):
    log_counter.labels(level="ERROR").inc()
    return {"message": f"severity with log level 'ERROR' and content: {error_message}"} 

@app.post("/log/critical")
async def log_endpoint_info(critical_message:Message):
    log_counter.labels(level="CRITICAL").inc()
    return {"message": f"severity with log level 'CRITICAL' and content: {critical_message}"} 

@app.get("/metrics")
async def metrics():
    # Collect latest Prometeues metrics and put them in format 'CONTENT_TYPE_LATEST'
    # Wrap response as scarlett 'Response' object since raw bytes are expected 
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)