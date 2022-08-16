from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from view import influencers, user

def include_router(app):
    app.include_router(influencers.router, prefix='/api/v1')
    app.include_router(user.router, prefix='/api/v1')

def start_application():
    app = FastAPI()
    include_router(app)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

app = start_application()
