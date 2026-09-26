from fastapi import APIRouter, Depends

from api.auth import authent
from api.public.proposal import views as proposals
from api.public.took_initiative import views as taken_initiatives

api = APIRouter()


api.include_router(
    proposals.router,
    prefix="/proposal",
    tags=["proposal"],
    dependencies=[],
)

api.include_router(
    taken_initiatives.router,
    prefix="/taken_initiative",
    tags=["TakenInitiative"],
    dependencies=[],
)
