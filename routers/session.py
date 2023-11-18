from fastapi import APIRouter, Depends
from ..models import SessionData
from ..dependencies import get_current_user

router = APIRouter(prefix="/session", tags=["session"])

@router.post("/save")
async def save_session(data: SessionData, current_user: User = Depends(get_current_user)):
    # Save session data
    return {"message": "Session saved"}

@router.get("/restore")
async def restore_session(current_user: User = Depends(get_current_user)):
    # Restore session data
    return SessionData()
