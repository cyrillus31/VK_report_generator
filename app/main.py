from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from schemas import RelatedUserOut
from services import VkUser
from celery_worker.tasks import PDF


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="static/templates")

@app.get("/")
async def root():
    return {"message": "This API allows you to generate PDF files with information about reltated users. (https://t.me/cyrillus31)"}


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


@app.get("/getFriendsWithGroupsREPORT", response_class=HTMLResponse)
async def get_friends_with_groups_and_generate_report(request: Request, user_id: int):
    user = VkUser(user_id)
    friends = await user.get_friends_with_groups()
    context={
                "user_id": user_id,
                "user_first_name": user.info["first_name"],
                "user_last_name": user.info["last_name"],
                "friends": friends
            }
           
    return templates.TemplateResponse(
            request=request,
            name="report.html",
            context=context
            )


@app.get("/getFriendsWithGroupsPDF", response_class=FileResponse)
async def get_friends_with_groups_and_generate_PDF(request: Request, user_id: int, background_task: BackgroundTasks):
    user = VkUser(user_id)
    friends = await user.get_friends_with_groups()
    context={
                "user_id": user_id,
                "user_first_name": user.info["first_name"],
                "user_last_name": user.info["last_name"],
                "friends": friends
            }
    pdf = PDF("report.html", f"{user_id}_report", context)
    background_task.add_task(pdf.delete)
    file_path = await pdf.create()
    return file_path








