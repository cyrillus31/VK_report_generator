import os

from pydantic_settings import BaseSettings

cwd = os.getcwd()

class Settings(BaseSettings):
    api_key: str 
    access_token: str

    rabbit_host: str 
    rabbit_port: int 
    rabbit_name: str
    rabbit_password: str
    
    database_password: str
    database_user: str
    database_host: str
    database_port: int

    pdf_storage_path: str = os.path.join(cwd, "PDF")

    class Config:
        env_file = os.path.join(cwd, ".env")

settings = Settings()
