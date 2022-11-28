from fastapi import FastAPI
from pydantic import BaseModel
from api_utils import model, log_data
class Input(BaseModel):
    x: float


app = FastAPI()


@app.get("/")
def ping():
    import time

    time.sleep(20)
    return {"y": "pong"}


@app.post("/predict/")
def api_prediction(input: Input):
    # parse input in appropriate format

    output = model.predict(input.x)  # model inference
    log_data(input.x, output)  # input/output logging to custom storage
    return {"y": output}
