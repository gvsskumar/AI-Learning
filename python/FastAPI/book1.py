from fastapi import FastAPI

app = FastAPI()

Books = [{'id': '1', 'title': 'The Great Gatsby', 'author': 'Kumar', 'category': 'Maths'},
        {'id': '2', 'title': 'The Pytghon Programming', 'author': 'Surya','category': 'Computers'}
        ]
@app.get("/")
async def root():
    try:
        return {"message": "Run the API with http://127.0.0.1:8000/books"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/books")
async def get_books():
    return Books

# book_id is a path parameter
# @app.get("/books/{book_id}")
# async def get_book(book_id: str):
#     for book in Books:
#         if book['id'] == book_id:
#             return book
        
# book_id is a path parameter another way
# @app.get("/books/{book_author}")        
# async def get_book(book_author: str):
#     for book in Books:
#         if book.get('author') == book_author:
#             return book


# GET book by author (query parameter)
@app.get("/books/")
async def get_book_by_author(author: str):
    for book in Books:
        if book["author"].lower() == author.lower():
            return book
    return {"message": "Book not found"}

# Get Dyna  mic Title and Query parameter
@app.get("/books/")
async def get_book_by_title(title: str):
    for book in Books:
        if book["title"].lower() == title.lower():
            return book
    return {"message": "Book not found"}

@app.get("/books/{author}/")
async def read_author_category_by_query(author: str, category: str):
    books_to_return = []
    for book in Books:
        if book.get("author").lower() == author.lower() and \
        book.get("category").lower() == category.lower():
             books_to_return.append(book)
             return books_to_return
    return {"message": "Book not found"}