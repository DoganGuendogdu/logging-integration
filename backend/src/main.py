from fastapi  import FastAPI
from pydantic import BaseModel

class Message(BaseModel):
    info_message:str

app = FastAPI()

@app.post("/log/info")
async def log_endpoint_info(info_message:Message):
    return {"message": f"severity with log level 'INFO' and content: {info_message}"} 

@app.post("/log/debug")
async def log_endpoint_info(debug_message:Message):
    return {"message": f"severity with log level 'DEBUG' and content: {debug_message}"} 

@app.post("/log/warning")
async def log_endpoint_info(warning_message:Message):
    return {"message": f"severity with log level 'WARNING' and content: {warning_message}"} 

@app.post("/log/error")
async def log_endpoint_info(error_message:Message):
    return {"message": f"severity with log level 'ERROR' and content: {error_message}"} 

@app.post("/log/critical")
async def log_endpoint_info(critical_message:Message):
    return {"message": f"severity with log level 'CRITICAL' and content: {critical_message}"} 
