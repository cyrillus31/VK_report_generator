from typing import Optional 
from pydantic import BaseModel


class RelatedUserIn(BaseModel): 
    id: int 
    original_user_id: int 
    social_network: str = "vkontakte"
    first_name: str = ""
    last_name: Optional[str] = ""
    about: Optional[str] = ""
    bdate: Optional[str] = "" 


class RelatedUserOut(BaseModel):
    id: int 
    social_network: str = "vkontakte"
    first_name: str
    last_name: str
    about: Optional[str] = "" 
    bdate: Optional[str] = "" 
    groups: Optional[list[dict | None | int | str]] = [] 

