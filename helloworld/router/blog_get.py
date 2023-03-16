from fastapi import APIRouter, Response, status
from enum import Enum
from typing import Optional


router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

@router.get('/all', 
         tags=['page'], 
         summary='Retrieve all blogs',
         )
def get_all_blog(page: int = 1, blog: Optional[str] = None):
    """
    ## This API is used to see how many pages a blog has.

    - **page** - int type, default value is 1, optional.
    - **blog** - str type, default value is None, optional
    """
    return {'message': f'Blog {blog} has {page} pages.'}

class BlogType(str, Enum):
    short = 'short'
    long = 'long'
    howto = 'howto'

@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type is {type}'}


@router.get('/{id}', status_code=status.HTTP_200_OK, tags=['response'])
def get_blog(id: int, res: Response):
    if id>5:
        res.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog with id {id} not found!'}
    else:
        return {'message': f'Blog with id {id}'}
