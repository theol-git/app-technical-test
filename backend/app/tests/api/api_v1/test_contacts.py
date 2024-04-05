from uuid import uuid4

from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.config import settings
from app.schemas.contact import ContactCreate
from tests.utils.utils import random_ascii_string


async def test_create_new_contact(client: AsyncClient) -> None:
    first_name = random_ascii_string()
    last_name = random_ascii_string()
    data = {"first_name": first_name, "last_name": last_name}

    response = await client.post(
        f"{settings.API_V1_STR}/contacts/",
        json=data,
    )

    assert response.status_code == 201
    data = response.json()
    assert data["first_name"] == first_name
    assert data["last_name"] == last_name


async def test_get_existing_contact(db_session: AsyncSession, client: AsyncClient) -> None:
    first_name = random_ascii_string()
    last_name = random_ascii_string()
    job = random_ascii_string()
    contact_in = ContactCreate(first_name=first_name, last_name=last_name, job=job)
    contact = await crud.create_contact(db_session, contact_in=contact_in)
    contact_id = contact.id

    response = await client.get(f"{settings.API_V1_STR}/contacts/{contact_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == str(contact_id)
    assert data["first_name"] == first_name
    assert data["last_name"] == last_name
    assert data["job"] == job


async def test_read_contacts(db_session: AsyncSession, client: AsyncClient) -> None:
    for _ in range(10):
        first_name = random_ascii_string()
        last_name = random_ascii_string()
        job = random_ascii_string()
        contact_in = ContactCreate(first_name=first_name, last_name=last_name, job=job)
        await crud.create_contact(db_session, contact_in=contact_in)

    response = await client.get(f"{settings.API_V1_STR}/contacts/")

    assert response.status_code == 200
    all_contacts = response.json()
    for contact in all_contacts:
        assert "id" in contact
        assert "first_name" in contact
        assert "last_name" in contact
        assert "job" not in contact


async def test_read_contact_not_found(client: AsyncClient) -> None:
    nonexistent_id = uuid4()

    response = await client.get(f"/contacts/{nonexistent_id}")

    assert response.status_code == 404
