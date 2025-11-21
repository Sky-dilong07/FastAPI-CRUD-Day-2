from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select

from database import engine, create_tables
from models import Book

# Create tables once when server starts
create_tables()

app = FastAPI()

@app.get("/books")
def get_books():
    with Session(engine) as session:
        books = session.exec(select(Book)).all()
        return books

@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book

@app.post("/books")
def create_book(new_book: Book):
    with Session(engine) as session:
        session.add(new_book)
        session.commit()
        session.refresh(new_book)
        return new_book


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")

        book.title = updated_book.title
        book.author = updated_book.author
        book.price = updated_book.price

        session.commit()
        session.refresh(book)
        return book


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")

        session.delete(book)
        session.commit()
        return {"message": "Book deleted successfully"}
