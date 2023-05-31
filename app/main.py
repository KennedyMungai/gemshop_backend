"""The entrypoint to the app"""
from fastapi import FastAPI
from sqlalchemy import create_engine

engine = create_engine('sqlite:///gemshop.db')


app = FastAPI(name='Gemshop Backend',
              description="The backend of a gemshop application")


@app.get("/", name="Root", description="The root endpoint for the application")
async def root() -> dict[str, str]:
    """The root endpoint for the application"""
    return {"message": "Hello World"}
