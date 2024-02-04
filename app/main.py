from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from schemas import RelatedUserOut
from services import VkUser


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="static/templates")

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


@app.get("/getFriendsWithGroupsPDF", response_class=HTMLResponse)
async def get_friends_with_groups_and_generate_PDF_report(request: Request, user_id: int):
    user = VkUser(user_id)
    friends = await user.get_friends_with_groups()
    context={
                "user_first_name": user.info["first_name"],
                "user_last_name": user.info["last_name"],
                "friends": friends
            }
           
    return templates.TemplateResponse(
            request=request,
            name="report.html",
            context=context
            )










