from fastapi import FastAPI
from router import blog_get


from starlette.responses import Response

app = FastAPI()
app.include_router(blog_get.router)

@app.get('/')
def index():
    return {'message': 'Hello world!'}


# @app.post('/hi')
# def index2():
#     return 'Hi'

