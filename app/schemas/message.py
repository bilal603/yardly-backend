from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MessageCreate(BaseModel):
    receiver_id: str
    product_id: str
    message: str

class MessageOut(BaseModel):
    id: str
    sender_id: str
    receiver_id: str
    product_id: str
    message: str
    timestamp: datetime
