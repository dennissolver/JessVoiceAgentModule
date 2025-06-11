from typing import Optional
import uuid

from fastapi import Depends
from fastapi_users import FastAPIUsers, schemas
from fastapi_users.manager import BaseUserManager
from fastapi_users.authentication import (
    BearerTransport, 
    AuthenticationBackend,
    JWTStrategy,
)
from fastapi_users.db import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTableUUID
from fastapi_users.password import PasswordHelper
from sqlalchemy import Column, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./users.db"

engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class User(SQLAlchemyBaseUserTableUUID, Base):
    username = Column(String, unique=True, nullable=False)

class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str

class UserCreate(schemas.BaseUserCreate):
    username: str

class UserUpdate(schemas.BaseUserUpdate):
    username: Optional[str] = None

async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

class UserManager(BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = "SECRET"
    verification_token_secret = "SECRET"

    async def on_after_register(self, user: User, request=None):
        pass

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")
SECRET = "SECRET"

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

current_active_user = fastapi_users.current_user(active=True)

async def create_db_and_admin():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with async_session_maker() as session:
        user_db = SQLAlchemyUserDatabase(session, User)
        user = await user_db.get_by_email("admin@example.com")
        if not user:
            helper = PasswordHelper()
            hashed = helper.hash("admin")
            await user_db.create(
                {
                    "email": "admin@example.com",
                    "hashed_password": hashed,
                    "username": "admin",
                    "is_active": True,
                    "is_superuser": True,
                }
            )
