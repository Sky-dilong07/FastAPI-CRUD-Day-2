from typing import Optional
from sqlmodel import SQLModel, Field 


# Optional allows the id to be empty when inserting
# SQLModel makes the class both Pydantic model + ORM model
# Field is used to define database column settings

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None,primary_key=True)  #when we create a book, we don't pass an ID — database generates it.
    title: str
    author: str
    price: float
