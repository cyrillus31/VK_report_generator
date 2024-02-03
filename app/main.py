from fastapi import FastAPI

from schemas import RelatedUserOut
from services import VkUser


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This API allows you to generate PDF files with information about reltated users."}


@app.get("/getFriends") # , response_model=list[RelatedUserOut])
async def get_friends(user_id: int):
    user = VkUser(user_id)
    response = await user.get_friends()
    return response 

    # return [{
    #         "id": 98712893712398,
    #         "social_network": "vkontakte",
    #         "first_name": "kirill",
    #         "last_name": "fed",
    #         "about": "lkjasdf",
    #         # "bdate": None,
    #         "link": "https://google.com"
    #         }
    #         ]




