from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello World!'}

@app.get('/blog/all')
def get_all_blog():
    return {'message': 'All blogs!'}

@app.get('/blog/{id}')
def get_blog(id: int):
    idx = id + 1
    return {'message': f'Blog with id {idx}'}

# @app.get('/blog/all')
# def get_all_blog():
#     return {'message': 'All blogs!'}


