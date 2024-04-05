# Import all the models, so that Base has them before being imported by Alembic

from .base_class import Base  # noqa: F401, I001

from app.models.contact import Contact  # noqa: F401
