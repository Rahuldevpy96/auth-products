from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import models
from .dependencies import get_current_user
from .routers import auth, products, session

app = FastAPI()

# Include routers
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(session.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Product Search API"}
