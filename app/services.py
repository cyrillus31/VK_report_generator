import httpx 

import json
from config import settings 

class VkUser:
    
    token = settings.access_token if settings.access_token else settings.api_key

    async def __init__(self, user_id, language: str = "ru"):
        self.user_id = user_id
        self.info = await self.get_user()
        self.language = language
        self.headers = {
                    "Authorization": f"Bearer {VkUser.token}",
                    "Accept-Language": f"{self.language}"
                }


    async def get_user(self) -> dict:
        async with httpx.AsyncClient() as client:
            url = f"https://api.vk.ru/method/users.get?user_ids={self.user_id}&v=5.131"
            r = await client.get(url, headers=self.headers)
        return r.json()["response"][0]

    async def get_friends(self) -> list:
        async with httpx.AsyncClient() as client:
            url = f"https://api.vk.ru/method/friends.get?user_id={self.user_id}&v=5.131&order=name"
            fields = ["sex", "about", "bdate"]
            params = {"fields": f"{','.join(fields)}"}
            r = await client.get(url, params=params, headers=self.headers)
        return r.json()["response"]["items"]

    async def get_groups(self, user_id=None) -> list:
        if not user_id:
            user_id = self.user_id
        async with httpx.AsyncClient() as client:
            url = f"https://api.vk.ru/method/groups.get?user_id={user_id}&v=5.131"
            params = {"extended": 0}
            r = await client.get(url, params=params, headers=self.headers)
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



