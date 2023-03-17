from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    pages: int
    published: Optional[bool]

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'version': version,
        'data': blog
        }

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int, 
                   comment_id: int = Query(None,
                        title="Id of the comment",
                        description="Some description for commend_id",
                        alias='commetId',
                        deprecated=True
                   ),
                #    comment:str = Body('This is default comment')
                #    comment:str = Body(...)
                   comment:str = Body(Ellipsis,
                                      min_length=10,
                                      max_length=50,
                                      regex='^[a-z\s]*$')
                ):
    return {
        'id': id,
        'commend_id': comment_id,
        # 'data': blog
        'blog': blog,
        'comment': comment
        }
