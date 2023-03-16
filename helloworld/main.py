from fastapi import FastAPI, Response, status
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello World!'}

@app.get('/blog/all', tags=['blog', 'page'])
def get_all_blog(page: int = 1, blog: Optional[str] = None):
    return {'message': f'Blog {blog} has {page} pages.'}

class BlogType(str, Enum):
    short = 'short'
    long = 'long'
    howto = 'howto'

@app.get('/blog/type/{type}', tags=['blog'])
def get_blog_type(type: BlogType):
    return {'message': f'Blog type is {type}'}


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog', 'response'])
def get_blog(id: int, res: Response):
    if id>5:
        res.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog with id {id} not found!'}
    else:
        return {'message': f'Blog with id {id}'}


