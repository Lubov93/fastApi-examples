from typing import Optional, List
from fastapi import APIRouter, Query, Body
from fastapi.param_functions import Body, Query
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    nb_comments: int

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version
    }

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int, 
        comment_id: int = Query(None,
        title='Id of comment',
        description='Some description for comment_id',
        alias='commentId',
        deprecated=True
        ),
        # content: str = Body('hi how are u?')
        content: str = Body(...,
        min_length=10,
        max_length=20,
        regex='^[a-z\s]*s'),
        v:Optional[List[str]] = Query(['1.0', '1.1', '1.2', '1.3'])
    ):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'content': content,
        'version': v
    }

