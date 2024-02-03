from datetime import date, datetime
from typing import Optional 
from pydantic import BaseModel, HttpUrl


class RelatedUserIn(BaseModel): 
    id: int 
    social_network: str = ""
    first_name: str = ""
    last_name: str = ""
    about: str = ""
    bdate: Optional[date] = "" 
    # link: Optional[HttpUrl] | None = None


class RelatedUserOut(BaseModel):
    id: int
    social_network: str = "vkontakte"
    first_name: str
    last_name: str
    about: str = "" 
    bdate: Optional[str] = "" 
    # link: Optional[HttpUrl] | None = None


print(RelatedUserOut)
