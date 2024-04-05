from uuid import uuid4

from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.schemas.contact import ContactCreate
from tests.utils.utils import random_ascii_string


async def test_create_contact(db_session: AsyncSession) -> None:
    first_name = random_ascii_string()
    last_name = random_ascii_string()
    job = random_ascii_string()
    contact_in = ContactCreate(first_name=first_name, last_name=last_name, job=job)

    contact = await crud.create_contact(db_session, contact_in=contact_in)

    assert contact.first_name == first_name
    assert contact.last_name == last_name
    assert contact.job == job


async def test_get_contact(db_session: AsyncSession) -> None:
    first_name = random_ascii_string()
    last_name = random_ascii_string()
    job = random_ascii_string()
    contact_in = ContactCreate(first_name=first_name, last_name=last_name, job=job)
    contact = await crud.create_contact(db_session, contact_in=contact_in)

    contact_out = await crud.get_contact(db_session, contact_id=contact.id)

    assert contact_out
    assert contact_out.id == contact.id
    assert contact_out.first_name == first_name
    assert contact_out.last_name == last_name
    assert contact_out.job == job


async def test_get_contact_nonexistent_id(db_session: AsyncSession) -> None:
    nonexistent_id = uuid4()

    contact = await crud.get_contact(db_session, contact_id=nonexistent_id)

    assert contact is None


async def test_get_all_contacts(db_session: AsyncSession) -> None:
    contact_count = 10
    for _ in range(contact_count):
        first_name = random_ascii_string()
        last_name = random_ascii_string()
        job = random_ascii_string()
        contact_in = ContactCreate(first_name=first_name, last_name=last_name, job=job)
        await crud.create_contact(db=db_session, contact_in=contact_in)

    contacts = await crud.get_contacts(db_session, skip=0, limit=contact_count)

    assert contacts
    assert len(contacts) == contact_count


async def test_get_contacts_paging(db_session: AsyncSession) -> None:
    contact_count = 10
    for _ in range(contact_count):
        first_name = random_ascii_string()
        last_name = random_ascii_string()
        job = random_ascii_string()
        contact_in = ContactCreate(first_name=first_name, last_name=last_name, job=job)
        await crud.create_contact(db=db_session, contact_in=contact_in)

    contacts = await crud.get_contacts(db_session, skip=0, limit=contact_count - 1)

    assert contacts
    assert len(contacts) == contact_count - 1
