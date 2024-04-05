from uuid import UUID

from pydantic import BaseModel, ConfigDict


# Shared properties
class ContactBase(BaseModel):
    first_name: str
    last_name: str
    job: str | None = None
    address: str | None = None
    question: str | None = None


# Properties to receive via API on creation
class ContactCreate(ContactBase):
    pass


# Properties to receive via API
class ContactOut(ContactBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
