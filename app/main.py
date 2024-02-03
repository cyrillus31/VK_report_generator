from fastapi import FastAPI

from schemas import RelatedUserOut


app = FastAPI()

@app.get("/")
def root():
    return {"message": "This API allows you to generate PDF files with information about reltated users."}


@app.get("/getFriends", response_model=list[RelatedUserOut])
def get_friends(user_id: int):
    # return {"message": f"Here will displaed a list of users with id: {user_id}"}
    return [{
            "id": 98712893712398,
            "social_network": "vkontakte",
            "first_name": "kirill",
            "last_name": "fed",
            "about": "lkjasdf",
            # "bdate": None,
            # "link": "https://google.com"
            }
            ]




