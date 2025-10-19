from fastapi import FastAPI, Body
from typing import Optional
from pydantic import BaseModel,Field
app = FastAPI()

class Book:
    id: Optional[int] = None
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
Books = [
    Book(id=1, title="Book 1", author="Surya", description="Description 1", rating=5),
    Book(id=2, title="Book 2", author="Kumar", description="Description 2", rating=4),
    Book(id=3, title="Book 3", author="John", description="Description 3", rating=3)
]

# GET all books
@app.get("/books")
async def get_books():
    return Books

# Create New Book
@app.post("/create")
async def create_book(book_request=Body()):
    Books.append(book_request)

# Create New Book another way
@app.post("/create-bbok")
async def createbook(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    Books.append(find_book_id(new_book))

def find_book_id(book:Book):
    book.id =1 if len(Books) == 0 else Books[-1].id + 1
    return book    