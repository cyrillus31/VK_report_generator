import httpx 

from config import settings 
from .friend_service import FriendService


# need to write a decorator that would retry sending requests for a certain amount of times until it gets through (because of the limit on 3 requests per second in VK api)

class VkUser:
    
    _token = settings.access_token if settings.access_token else settings.api_key

    def __init__(self, user_id, language: str = "ru"):
        self.user_id = user_id
        self.headers = {
                    "Authorization": f"Bearer {VkUser._token}",
                    "Accept-Language": f"{language}"
                }
        self.info = self.get_user()

    def get_user(self) -> dict:
        with httpx.Client() as client:
            url = f"https://api.vk.ru/method/users.get?user_ids={self.user_id}&v=5.131"
            r = client.get(url, headers=self.headers)
            print(r.json())
        return r.json()["response"][0]

    async def _get_friends_from_other_networks(self) -> list:
        other_friends = await FriendService.get(self.user_id)
        return other_friends

    async def get_friends(self) -> list:
        async with httpx.AsyncClient() as client:
            url = f"https://api.vk.ru/method/friends.get?user_id={self.user_id}&v=5.131&order=name"
            fields = ["sex", "about", "bdate"]
            params = {"fields": f"{','.join(fields)}"}
            r = await client.get(url, params=params, headers=self.headers)
            friends = r.json()["response"]["items"]
        other_friends = await self._get_friends_from_other_networks()
        return other_friends + friends
 
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



