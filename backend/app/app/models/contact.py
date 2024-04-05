from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base_class import Base


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    first_name: Mapped[str] = mapped_column(index=True, nullable=False)
    last_name: Mapped[str] = mapped_column(index=True, nullable=False)
    job: Mapped[str | None]
    address: Mapped[str | None]
    question: Mapped[str | None]
