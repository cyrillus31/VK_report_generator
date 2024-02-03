import httpx 

import json
from config import settings 

class VkUser:
    
    token = settings.access_token if settings.access_token else settings.api_key

    def __init__(self, user_id):
        self.user_id = user_id

    async def get_friends(self) -> list:
        async with httpx.AsyncClient() as client:
            url = f"https://api.vk.ru/method/friends.get?user_id={self.user_id}&v=5.131&order=name"
            headers = {"Authorization": f"Bearer {VkUser.token}"}

            params = {"fields": "sex, about, bdate"}
            r = await client.get(url, params=params, headers=headers)
            return r.json()["response"]["items"]

    async def get_groups(self, user_id=None) -> list:
        if not user_id:
            user_id = self.user_id
        async with httpx.AsyncClient() as client:
            url = f"https://api.vk.ru/method/groups.get?user_id={user_id}&v=5.131"
            headers = {"Authorization": f"Bearer {VkUser.token}"}
            params = {"extended": 0}
            r = await client.get(url, params=params, headers=headers)
            try:
                return r.json()["response"]["items"]
            except KeyError:
                return []

    async def get_friends_with_groups(self) -> list:
        friends = await self.get_friends()
        for friend in friends:
            friend_id = int(friend["id"])
            groups = await self.get_groups(user_id=friend_id)
            friend["groups"] = groups
        return friends



