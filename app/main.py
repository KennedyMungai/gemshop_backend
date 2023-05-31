"""The entrypoint to the app"""
from fastapi import FastAPI

from database.db import create_db_and_tables

app = FastAPI(name='Gemshop Backend',
              description="The backend of a gemshop application")


@app.on_event("startup")
def startup():
    """Called on app startup"""
    print("Starting up")
    create_db_and_tables()


@app.get("/", name="Root", description="The root endpoint for the application")
async def root() -> dict[str, str]:
    """The root endpoint for the application"""
    return {"message": "Hello World"}
