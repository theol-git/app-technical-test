from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db_session
from app.crud import create_contact, get_contact, get_contacts
from app.schemas.contact import ContactCreate, ContactOut

router = APIRouter()


@router.post("/", status_code=201)
async def create_contact_endpoint(contact_in: ContactCreate, db: AsyncSession = Depends(get_db_session)) -> ContactOut:
    return await create_contact(db=db, contact_in=contact_in)


@router.get("/{contact_id}")
async def read_contact_endpoint(contact_id: UUID, db: AsyncSession = Depends(get_db_session)) -> ContactOut:
    contact = await get_contact(db=db, contact_id=contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.get("/", response_model_exclude_none=True)
async def read_contacts_endpoint(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db_session)
) -> list[ContactOut]:
    return await get_contacts(db=db, skip=skip, limit=limit)
