from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.config import Settings
from api.database import create_db_and_tables
from api.public import api as public_api
from api.utils.logger import logger_config
from api.utils.mock_data_generator import create_proposals_and_taken_initiatives

logger = logger_config(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    create_proposals_and_taken_initiatives()

    logger.info("startup: triggered")

    yield

    logger.info("shutdown: triggered")


def create_app(settings: Settings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/",
        description=settings.DESCRIPTION,
        lifespan=lifespan,
    )
    origins = [*
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    #"http://localhost",
        "http://localhost:8080",
        "http://localhost:1111",

]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,# True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(public_api)

    return app
