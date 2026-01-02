# from pydantic_settings import BaseSettings  # Pydantic 2.x ke liye
# from pydantic import Field

# class Settings(BaseSettings):
#     DB_HOST: str = Field(..., description="AWS RDS hostname or IP")
#     DB_USER: str = Field(..., description="Database username")
#     DB_PASSWORD: str = Field(..., description="Database password")
#     DB_NAME: str = Field(..., description="Database name")

#     class Config:
#         env_file = ".env"          # .env file se secrets load karega
#         env_file_encoding = "utf-8" # Encoding safe rakho

# # Global settings object
# settings = Settings()


# app/core/config.py
# from pydantic_settings import BaseSettings  # Correct package for Pydantic 2.x
# from pydantic import Field

# class Settings(BaseSettings):
#     DB_HOST: str = Field(..., description="AWS RDS hostname or IP")
#     DB_USER: str = Field(..., description="Database username")
#     DB_PASSWORD: str = Field(..., description="Database password")
#     DB_NAME: str = Field(..., description="Database name")

#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"

# # Global settings object
# settings = Settings()/


from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    DB_HOST: str = Field(..., description="AWS RDS hostname or IP")
    DB_USER: str = Field(..., description="Database username")
    DB_PASSWORD: str = Field(..., description="Database password")
    DB_NAME: str = Field(..., description="Database name")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Global settings object
settings = Settings()


