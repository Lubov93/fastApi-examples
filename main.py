from fastapi import FastAPI
from router import blog_get
from router import blog_post


from starlette.responses import Response

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/')
def index():
    return {'message': 'Hello world!'}


# @app.post('/hi')
# def index2():
#     return 'Hi'

