from fastapi import FastAPI

app = FastAPI()

from app.routes import auth
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Yardly API is running"}

from app.routes import messages
app.include_router(messages.router)