from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import Mapped, mapped_column



class Base(DeclarativeBase):
    pass

class Friend(Base):
    __tablename__ = "friend"

    id: Mapped[str] = mapped_column(primary_key=True)
    original_user_id: Mapped[str] = mapped_column(String(50))
    social_network: Mapped[str] = mapped_column(String(30))
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50), default="")
    about: Mapped[str] = mapped_column(String(500), default="No data")
    bdate: Mapped[str] = mapped_column(String(50), default="No date")
