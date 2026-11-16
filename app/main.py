from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI(title="RabbitMQ Lab 7") 

class OrderRequest(BaseModel): 
    order_id: int 
    product: str 
    quantity: int 

@app.post("/orders", status_code=200) 
async def submit_order(order: OrderRequest): 
    return {"status": "received", "order_id": order.order_id}