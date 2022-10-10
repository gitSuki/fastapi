from fastapi import FastAPI
from enum import Enum

app = FastAPI()

BOOKS = {
  'book_1' : {'title' : 'title_one', 'author' : 'author_one'},
  'book_2' : {'title' : 'title_two', 'author' : 'author_two'},
  'book_3' : {'title' : 'title_three', 'author' : 'author_three'},
  'book_4' : {'title' : 'title_four', 'author' : 'author_four'},
  'book_5' : {'title' : 'title_five', 'author' : 'authorfive'},
}

class DirectionName(str, Enum):
  north = 'North'
  south = 'South'
  east = 'East'
  west = 'West'

@app.get('/books/all')
async def get_all_books():
  return BOOKS

@app.get('/books/my_book')
async def get_favorite_book():
  return {'book_title' : 'My favorite book'}

@app.get('/books/{book_id}')
async def get_book(book_id: int):
  return {'book_title' :  book_id}

@app.get('/directions/{direction_name}')
async def get_direction(direction_name: DirectionName):
  if direction_name == DirectionName.north:
    return {"Direction": direction_name, "sub": "up"}
  if direction_name == DirectionName.south:
    return {"Direction": direction_name, "sub": "down"}
  if direction_name == DirectionName.west:
    return {"Direction": direction_name, "sub": "left"}
  if direction_name == DirectionName.east:
    return {"Direction": direction_name, "sub": "right"}