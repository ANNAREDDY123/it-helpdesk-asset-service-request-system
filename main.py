import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

from routes.auth import router as auth_router
from routes.assets import router as assets_router
from routes.requests import router as requests_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="IT Helpdesk Asset Service Request System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(assets_router)
app.include_router(requests_router)


@app.get("/")
def home():

    logger.info("Application Started Successfully")

    return {
        "message": "IT Helpdesk Asset Service Request System"
    }
