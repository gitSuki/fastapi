from typing import Optional
from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    'book_1': {'id': 1, 'title': 'title_one', 'author': 'author_one'},
    'book_2': {'id': 2, 'title': 'title_two', 'author': 'author_two'},
    'book_3': {'id': 3, 'title': 'title_three', 'author': 'author_three'},
    'book_4': {'id': 4, 'title': 'title_four', 'author': 'author_four'},
    'book_5': {'id': 5, 'title': 'title_five', 'author': 'author_five'},
}


@app.get('/books/all')
async def get_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get('/books/{book_id}')
async def get_book(book_id: int):
    for book in BOOKS.values():
        if book['id'] == book_id:
            return book


@app.post('/')
async def create_book(book_title, book_author):
    current_book_id = 0

    # getting highest ID
    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book_id:
                current_book_id = x
    current_book_id += 1

    # adding new book
    BOOKS[f'book_{current_book_id}'] = {
        'id': current_book_id,
        'title': book_title,
        'author': book_author}
    return BOOKS[f'book_{current_book_id}']


@app.put('/{book_name}')
async def update_book(book_name: str, book_title: str, book_author: str):
    book_info = {'title': book_title, 'author': book_author}
    BOOKS[book_name] = book_info
    return book_info


@app.delete('/{book_name}')
async def delete_book(book_name: str):
    del BOOKS[book_name]
    return f'Book {book_name} deleted'
