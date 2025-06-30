from fastapi import FastAPI
from src.api.v1 import auth, users, stories
from src.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(stories.router, prefix="/api/v1/stories", tags=["Stories"])

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Personalized Bedtime Story App Backend!"}
