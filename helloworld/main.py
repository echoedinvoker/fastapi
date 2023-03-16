from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello World!'}

@app.get('/blog/all')
# def get_all_blog(page: int = 1, blog: str = 'test'):
def get_all_blog(page: int = 1, blog: Optional[str] = None):
    # return {'message': 'All blogs!'}
    return {'message': f'Blog {blog} has {page} pages.'}

class BlogType(str, Enum):
    short = 'short'
    long = 'long'
    howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type is {type}'}


@app.get('/blog/{id}')
def get_blog(id: int):
    idx = id + 1
    return {'message': f'Blog with id {idx}'}


