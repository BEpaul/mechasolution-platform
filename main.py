from fastapi import FastAPI
import uvicorn

from view import influencers, user

def include_router(app):
    app.include_router(influencers.router, prefix='/app/v1')
    app.include_router(user.router, prefix='/app/v1')

def start_application():
    app = FastAPI()
    include_router(app)

    return app

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

app = start_application()
