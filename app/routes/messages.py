from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.message import MessageCreate, MessageOut
from app.utils.token import verify_token
from fastapi.security import OAuth2PasswordBearer
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import os
from bson import ObjectId
from app.models.message import message_dict

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client.yardly
messages_collection = db.messages

async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return payload["sub"]

@router.post("/messages/send", response_model=MessageOut)
async def send_message(data: MessageCreate, current_user: str = Depends(get_current_user)):
    message = {
        "sender_id": ObjectId(current_user),
        "receiver_id": ObjectId(data.receiver_id),
        "product_id": ObjectId(data.product_id),
        "message": data.message,
        "timestamp": datetime.utcnow()
    }
    result = await messages_collection.insert_one(message)
    saved_message = await messages_collection.find_one({"_id": result.inserted_id})
    return message_dict(saved_message)

@router.get("/messages/{conversation_id}", response_model=list[MessageOut])
async def get_conversation(conversation_id: str, current_user: str = Depends(get_current_user)):
    messages = messages_collection.find({
        "$or": [
            {"sender_id": ObjectId(current_user), "receiver_id": ObjectId(conversation_id)},
            {"sender_id": ObjectId(conversation_id), "receiver_id": ObjectId(current_user)}
        ]
    }).sort("timestamp", 1)

    result = []
    async for msg in messages:
        result.append(message_dict(msg))
    return result
