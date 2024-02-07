from typing import Optional 
from pydantic import BaseModel, HttpUrl


class RelatedUserIn(BaseModel): 
    id: str 
    social_network: str = ""
    first_name: str = ""
    last_name: Optional[str] = ""
    about: Optional[str] = ""
    bdate: Optional[str] = "" 
    # link: Optional[HttpUrl] | None = None


class RelatedUserOut(BaseModel):
    id: str 
    social_network: str = "vkontakte"
    first_name: str
    last_name: str
    about: Optional[str] = "" 
    bdate: Optional[str] = "" 
    groups: Optional[list[dict | None | int]] = [] 
    # link: Optional[HttpUrl] | None = None

