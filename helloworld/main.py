from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse, PlainTextResponse
from exceptions import StoryException
from router import blog_get
from router import blog_post
from router import user
from router import article
from db import models
from db.database import engine


app = FastAPI()
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


