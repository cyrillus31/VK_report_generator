import httpx 

from config import settings 

class VkUser:
    def __init__(self, user_id):
        self.user_id = user_id

    async def get_friends(self):
        async with httpx.AsyncClient() as client:
            url = f"https://api.vk.ru/method/friends.get?user_id={self.user_id}&v=5.131&order=name"
            headers = {"Authorization": f"Bearer {settings.api_key}"}

            params = {"fields": "sex, about, bdate"}
            r = await client.get(url, params=params, headers=headers)
            return r.json()["response"]["items"]

    async def get_groupds(self):
        async with httpx.AsyncClient() as client:
            url = f"https://api.vk.ru/method/groups.get?user_id={self.user_id}&v=5.131"
            headers = {"Authorization": f"Bearer {settings.api_key}"}

            # params = {"extended": 1}
            params = {}
            r = await client.get(url, params=params, headers=headers)
            return r.json()


