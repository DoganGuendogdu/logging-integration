from fastapi  import FastAPI
from pydantic import BaseModel
from prometheus_client import Counter, Gauge
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response


log_counter = Counter("log_events_total", "Counts number of entries for every log level", ["level"])
costs_total = Gauge("costs_total", "Summarizes total costs for different customers", ["customer"])

class Message(BaseModel):
    message:str

class Costs(BaseModel):
    cost:str

app = FastAPI()

@app.post("/log/info")
async def log_endpoint_info(message:Message):
    log_counter.labels(level="INFO").inc()
    return {"message": f"severity with log level 'INFO' and content: {message}"} 

@app.post("/log/debug")
async def log_endpoint_info(message:Message):
    log_counter.labels(level="DEBUG").inc()
    return {"message": f"severity with log level 'DEBUG' and content: {message}"} 

@app.post("/log/warning")
async def log_endpoint_info(message:Message):
    log_counter.labels(level="WARNING").inc()
    return {"message": f"severity with log level 'WARNING' and content: {message}"} 

@app.post("/log/error")
async def log_endpoint_info(message:Message):
    log_counter.labels(level="ERROR").inc()
    return {"message": f"severity with log level 'ERROR' and content: {message}"} 

@app.post("/log/critical")
async def log_endpoint_info(message:Message):
    log_counter.labels(level="CRITICAL").inc()
    return {"message": f"severity with log level 'CRITICAL' and content: {message}"} 

@app.post("/cost/vodafone")
async def cost_vodafone(cost: Costs):
    costs_total.labels(customer="Vodafone").set(cost.cost)
    return {"cost_vodafone": cost}
    
@app.post("/cost/telekom")
async def cost_telekom(cost:Costs):
    costs_total.labels(customer="Telekom").set(cost.cost)
    return {"cost_telekom": cost}

@app.post("/cost/1und1")
async def cost_1und1(cost: Costs):
    costs_total.labels(customer="1und1").set(cost.cost)
    return {"cost_1und1": cost}

@app.get("/metrics")
async def metrics():
    # Collect latest Prometeues metrics and put them in format 'CONTENT_TYPE_LATEST'
    # Wrap response as scarlett 'Response' object since raw bytes are expected 
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)