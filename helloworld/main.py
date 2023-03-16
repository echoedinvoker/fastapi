from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello World!'}

@app.get('/blog/all')
def get_all_blog():
    return {'message': 'All blogs!'}

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


