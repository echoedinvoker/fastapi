from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    pages: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1', 'val1'}
    image: Optional[Image] = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'version': version,
        'data': blog
        }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int, 
                   comment_title: str = Query(None,
                        title="Id of the comment",
                        description="Some description for commend_id",
                        alias='commetTitle',
                        deprecated=True
                   ),
                   comment:str = Body(Ellipsis,
                                      min_length=10,
                                      max_length=50,
                                      regex='^[a-z\s]*$'),
                                      v: Optional[List[str]]=Query(['1.1','1.2','2.1']),
                    comment_id:int = Path(None, gt=5, le=10)
                        
                    ):
    return {
        'id': id,
        'commend_title': comment_title,
        'blog': blog,
        'comment': comment,
        'version': v,
        'comment_id': comment_id
        }
