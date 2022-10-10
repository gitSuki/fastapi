from fastapi import FastAPI
from enum import Enum

app = FastAPI()

BOOKS = {
  'book_1' : {'id' : 1, 'title' : 'title_one', 'author' : 'author_one'},
  'book_2' : {'id' : 2, 'title' : 'title_two', 'author' : 'author_two'},
  'book_3' : {'id' : 3, 'title' : 'title_three', 'author' : 'author_three'},
  'book_4' : {'id' : 4, 'title' : 'title_four', 'author' : 'author_four'},
  'book_5' : {'id' : 5, 'title' : 'title_five', 'author' : 'authorfive'},
}

@app.get('/books/all')
async def get_all_books():
  return BOOKS

@app.get('/books/{book_id}')
async def get_book(book_id: int):
  for book in BOOKS.values():
    if book['id'] == book_id:
      return book