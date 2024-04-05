from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import sessionmanager


async def get_db_session() -> AsyncSession:
    async with sessionmanager.session() as session:
        yield session
