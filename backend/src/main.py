import subprocess
from pathlib import Path

from dotenv import dotenv_values
from fastapi import FastAPI
from prometheus_client import Counter, Gauge
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from pydantic import BaseModel
from starlette.responses import Response

from .json_file_manipulation import *

logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.DEBUG)

log_counter = Counter("log_events_total", "Counts number of entries for every log level", ["level"])
costs_total = Gauge("costs_total", "Summarizes total costs for different customers", ["customer"])

PROJECT_DIR_PATH = Path(__file__).parent.parent.parent
BACKEND_DIR_PATH = PROJECT_DIR_PATH / "backend"

try:
    config = dotenv_values(BACKEND_DIR_PATH / ".env")
except FileNotFoundError as e:
    raise e

CONFIG_FILE_DIR = Path(str(config.get("CONFIG_FILE_DIR")))
SCRIPTS_DIR = Path(str(config.get("SCRIPTS_DIR")))

CONFIG_FILE = CONFIG_FILE_DIR / "config.json"
CREATE_PROMETHEUS_ALERT_SCRIPT = SCRIPTS_DIR / "create-prometheus-alerts.sh"


class Message(BaseModel):
    message: str


# stores generated costs
class Costs(BaseModel):
    cost: str


# stores thresholds
class ThresholdCosts(BaseModel):
    total_costs: float
    vodafone_cost: float
    telekom_cost: float
    cost_1und1: float


app = FastAPI(debug=True)


@app.post("/log/info")
async def log_endpoint_info(message: Message):
    log_counter.labels(level="INFO").inc()
    return {"message": f"severity with log level 'INFO' and content: {message}"}


@app.post("/log/debug")
async def log_endpoint_info(message: Message):
    log_counter.labels(level="DEBUG").inc()
    return {"message": f"severity with log level 'DEBUG' and content: {message}"}


@app.post("/log/warning")
async def log_endpoint_info(message: Message):
    log_counter.labels(level="WARNING").inc()
    return {"message": f"severity with log level 'WARNING' and content: {message}"}


@app.post("/log/error")
async def log_endpoint_info(message: Message):
    log_counter.labels(level="ERROR").inc()
    return {"message": f"severity with log level 'ERROR' and content: {message}"}


@app.post("/log/critical")
async def log_endpoint_info(message: Message):
    log_counter.labels(level="CRITICAL").inc()
    return {"message": f"severity with log level 'CRITICAL' and content: {message}"}


# TODO: Add thresholds as metric
@app.post("/threshold/costs")
async def threshold_costs(threshold_cost: ThresholdCosts):
    logger.debug(f"Cost thresholds: {threshold_cost}")

    threshold_data_json = {
        "total_cost": threshold_cost.total_costs,
        "vodafone_cost": threshold_cost.vodafone_cost,
        "telekom_cost": threshold_cost.telekom_cost,
        "1und1_cost": threshold_cost.cost_1und1
    }

    config_file_data = read_contents_from_json_file(CONFIG_FILE)
    config_file_with_replaced_data = replace_values_json_file(config_file_data, threshold_data_json, "thresholds")
    write_contents_to_json_file(CONFIG_FILE, config_file_with_replaced_data)

    try:
        subprocess.run(CREATE_PROMETHEUS_ALERT_SCRIPT)
    except Exception as e:
        logger.error(f"Error while creating 'alert-rules.yml': {e}")
        raise e

    return threshold_data_json


@app.post("/cost/vodafone")
async def cost_vodafone(cost: Costs):
    costs_total.labels(customer="Vodafone").inc(float(cost.cost))
    logger.debug(f"Costs for Vodafone: {cost.cost}")
    return {"cost_vodafone": cost}


@app.post("/cost/telekom")
async def cost_telekom(cost: Costs):
    costs_total.labels(customer="Telekom").inc(float(cost.cost))
    logger.debug(f"Costs for Telekom: {cost.cost}")
    return {"cost_telekom": cost}


@app.post("/cost/1und1")
async def cost_1und1(cost: Costs):
    costs_total.labels(customer="1und1").inc(float(cost.cost))
    logger.debug(f"Costs for 1und1: {cost.cost}")
    return {"cost_1und1": cost}


@app.get("/metrics")
async def metrics():
    # Collect latest Prometeues metrics and put them in format 'CONTENT_TYPE_LATEST'
    # Wrap response as scarlett 'Response' object since raw bytes are expected 
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
