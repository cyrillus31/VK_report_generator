# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.orm import sessionmaker


from config import settings

# DB_URL = f"postgresql://{settings.database_user}:{settings.database_password}@{settings.database_host}/related_users"
DB_URL = f"postgresql+asyncpg://{settings.database_user}:{settings.database_password}@{settings.database_host}:{settings.database_port}/related_users"

# engine = create_async_engine(DB_URL, echo=True)
# 
# async_session = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession, expire_on_commit=False)
# 
# async def get_session() -> AsyncSession:
#     async with async_session() as session:
#         yield session
