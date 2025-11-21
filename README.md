🚀 Day 2 — FastAPI CRUD with Database (SQLModel + SQLite)
📌 Description

This version upgrades the Day 1 API to use a real database (SQLite) with SQLModel, a modern ORM combining SQLAlchemy + Pydantic.

🗂 Folder Structure
Day_2/
 ├─ database.py
 ├─ models.py
 ├─ schemas.py
 ├─ main.py

🧾 Endpoints
Method	Endpoint	Description
GET	/books/	Get all books
GET	/books/{book_id}	Get a single book
POST	/books/	Create a book
PUT	/books/{book_id}	Update a book
DELETE	/books/{book_id}	Delete a book
🗄 Database Model (SQLModel)
class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    description: str
    price: float
    created_at: datetime

📘 Schemas (Pydantic + SQLModel approach)

BookCreated → POST payload

BookUpdate → PUT payload (partial update supported)

BookResponse → Response model for all API outputs

▶️ Run Instructions
uvicorn main:app --reload


Swagger UI → http://127.0.0.1:8000/docs

🧠 Skills Learned

SQLModel ORM modeling

Database session with Session and Depends

Writing CRUD using select(), session.get(), add(), commit(), refresh()

Using dedicated request/response schemas

Persistent data storage with SQLite
