from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.contact import Contact as ContactDBModel
from app.schemas.contact import ContactCreate, ContactOut


async def create_contact(db: AsyncSession, *, contact_in: ContactCreate) -> ContactOut:
    db_obj = ContactDBModel(**contact_in.model_dump())
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return ContactOut.model_validate(db_obj)


async def get_contact(db: AsyncSession, *, contact_id: UUID) -> ContactOut | None:
    result = await db.execute(select(ContactDBModel).filter(ContactDBModel.id == contact_id))
    contact = result.scalars().first()

    if not contact:
        return None

    return ContactOut.model_validate(contact)


async def get_contacts(db: AsyncSession, *, skip: int, limit: int) -> list[ContactOut]:
    result = await db.execute(
        select(ContactDBModel.id, ContactDBModel.first_name, ContactDBModel.last_name).offset(skip).limit(limit)
    )
    contacts = result.fetchall()
    return [ContactOut.model_validate(contact) for contact in contacts]
