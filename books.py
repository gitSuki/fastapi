from fastapi import FastAPI

app = FastAPI()

BOOKS = {
  'book_1' : {'title' : 'title_one', 'author' : 'author_one'},
  'book_2' : {'title' : 'title_two', 'author' : 'author_two'},
  'book_3' : {'title' : 'title_three', 'author' : 'author_three'},
  'book_4' : {'title' : 'title_four', 'author' : 'author_four'},
  'book_5' : {'title' : 'title_five', 'author' : 'authorfive'},
}

@app.get('/')
async def read_all_books():
  return  