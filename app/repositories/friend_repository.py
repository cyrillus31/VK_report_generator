from sqlalchemy import select

from models import Friend
from database import get_session

class FriendRepository:
    def __init__(
            self,
            id: int,
            original_user_id: str,
            social_network: str,
            first_name: str,
            last_name: str,
            about: str,
            bdate: str
            ):
        self.id = id
        self.original_user_id = original_user_id
        self.social_network = social_network
        self.first_name = first_name
        self.last_name = last_name
        self.about = about
        self.bdate = bdate

    async def add(self):
        friend = Friend(
                id = self.id,
                original_user_id = self.original_user_id,
                social_network = self.social_network,
                first_name = self.first_name,
                last_name = self.last_name,
                about = self.about,
                bdate = self.bdate,
                )
        async with get_session() as session:
            session.add(friend)
            await session.commit()

    @classmethod 
    async def get(cls, original_user_id: int) -> list[None | Friend]:
        stmt = select(Friend).where(Friend.original_user_id == original_user_id)
        async with get_session() as session:
            result = await session.execute(stmt)
        result = [friend for friend in result.scalars()]
        return result







