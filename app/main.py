from fastapi import FastAPI

from schemas import RelatedUserOut
from services import VkUser


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This API allows you to generate PDF files with information about reltated users."}


@app.get("/getFriends", response_model=list[RelatedUserOut])
async def get_friends(user_id: int):
    user = VkUser(user_id)
    response = await user.get_friends()
    return response 


@app.get("/getGroups", response_model=list[RelatedUserOut])
async def get_groups(user_id: int):
    user = VkUser(user_id)
    response = await user.get_groups()
    return response 


@app.get("/getFriendsWithGroups", response_model=list[RelatedUserOut])
async def get_friends_with_groups(user_id: int):
    user = VkUser(user_id)
    response = await user.get_friends_with_groups()
    return response


