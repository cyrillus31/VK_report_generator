import httpx 

from config import settings 

class VkUser:
    def __init__(self, user_id):
        self.user_id = user_id

    async def get_friends(self, language: str = "ru", **params):
        async with httpx.AsyncClient() as client:
            url = f"https://api.vk.ru/method/friends.get?user_id={self.user_id}&v=5.131&order=name"
            headers = {"Authorization": f"Bearer {settings.api_key}"}

            r = await client.get(url, params=params, headers=headers)
            return r.json()


