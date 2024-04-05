from fastapi import APIRouter

from app.api.api_v1.endpoints import contacts

api_router = APIRouter()
api_router.include_router(
    contacts.router,
    prefix="/contacts",
    tags=["contacts"],
)
