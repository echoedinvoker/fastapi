from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse, PlainTextResponse
from exceptions import StoryException
from router import blog_get
from router import blog_post
from router import user
from router import article
from router import product
from db import models
from db.database import engine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(product.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/')
def index():
    return {'message': 'Hello World!'}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
            status_code=418,
            content={'detail': exc.name}
            )

@app.exception_handler(HTTPException)
def custom_exc_handler(request: Request, exc: HTTPException):
    return PlainTextResponse(
            exc.detail,             
            status_code=status.HTTP_400_BAD_REQUEST
            )

models.Base.metadata.create_all(engine)

origins = [
        'http://localhost:3001'
        ]

app.add_middleware(
        CORSMiddleware,
        allow_origins = origins,
        allow_credentials = True,
        allow_methods = ['*'],
        allow_headers = ['*']
        )
