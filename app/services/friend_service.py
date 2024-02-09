from fastapi import Depends

from repositories import FriendRepository
from schemas import RelatedUserIn
from models import Friend


class FriendService:
    def __init__(self, friend_data: RelatedUserIn = Depends()):
        self.friend_repository = FriendRepository(**friend_data.dict())
        self.original_user_id = friend_data.original_user_id

    async def add(self):
        await self.friend_repository.add()
    
    @classmethod
    async def get(cls, original_user_id: int):
        try:
            original_user_id = int(original_user_id)
        except ValueError:
            raise Exception("Invalid original_user_id. Supposed to be an integer.")
        else:
            list_of_friends: list[None | Friend] = await FriendRepository.get(original_user_id)
            return list_of_friends


