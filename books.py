import imp
from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional
app=FastAPI()

class Book(BaseModel):
    id : UUID
    title:str = Field(min_length =1)
    author:str = Field(min_length =1,max_length =100)
    description: Optional[str] = Field(title ="description of Book",
                            max_length =100,
                            min_length =2)
    rating:int = Field(gt = -1,lt =101)

    # class Config:
    #     Schema_extra = {
    #         "example":{
    #             "id":"1fa85f65-5717-4562-b3fc-2c963f66afa6",
    #             "title":"new_book",
    #             "author":"Sush_Brown",
    #             "description": "This is a new book",
    #             "rating": 75
    #         }
    #     }

BOOKS=[]

@app.get('/')
async def readAllBook():
    if len(BOOKS) < 1:
        create_book_no_api()
    return BOOKS

@app.post('/')
async def create_Book(book:Book):
    BOOKS.append(book)
    return book

def create_book_no_api():
    book1 = Book(id = "3fa85f65-5717-4562-b3fc-2c963f66afa6",
        title = "Book1",
        author = "AT1",
        description = "this is book 1",
        rating =  60)
    book2 = Book(id = "3fa85f66-5717-4562-b3fc-2c963f66afa6",
        title = "Book2",
        author = "AT2",
        description = "this is book 2",
        rating = 80)   
    book3 = Book(id = "3fa85f67-5717-4562-b3fc-2c963f66afa6",
        title = "Book3",
        author = "AT3",
        description ="this is book 3",
        rating = 40)
    book4 = Book(id =  "3fa85f68-5717-4562-b3fc-2c963f66afa6",
        title = "Book4",
        author = "AT4",
        description = "this is book 4",
        rating = 50)
    BOOKS.append(book1)
    BOOKS.append(book2)
    BOOKS.append(book3)
    BOOKS.append(book4)