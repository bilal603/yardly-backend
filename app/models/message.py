def message_dict(message: dict):
    return {
        "id": str(message["_id"]),
        "sender_id": str(message["sender_id"]),
        "receiver_id": str(message["receiver_id"]),
        "product_id": str(message["product_id"]),
        "message": message["message"],
        "timestamp": message["timestamp"]
    }
