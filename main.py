from fastapi import FastAPI
from router import blog_get
from router import blog_post
from db import models
from db.database import engine

from starlette.responses import Response

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/')
def index():
    return {'message': 'Hello world!'}


models.Base.metadata.create_all(engine)  # Create our DB

# @app.post('/hi')
# def index2():
#     return 'Hi'
