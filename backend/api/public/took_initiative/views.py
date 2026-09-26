from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from api.database import get_session
from api.public.took_initiative.crud import (
    create_taken_initiative,
    delete_taken_initiative,
    read_taken_initiative,
    read_taken_initiatives,
)
from api.public.took_initiative.models import TakenInitiativeCreate, TakenInitiativeRead

router = APIRouter()


@router.post("", response_model=TakenInitiativeRead)
def create_a_taken_initiative(taken_initiative: TakenInitiativeCreate, db: Session = Depends(get_session)):
    return create_taken_initiative(taken_initiative=taken_initiative, db=db)

@router.get("", response_model=list[TakenInitiativeRead])
def get_taken_initiatives(
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    db: Session = Depends(get_session),
):
    return read_taken_initiatives(offset=offset, limit=limit, db=db)

@router.get("/{taken_initiative_id}", response_model=TakenInitiativeRead)
def get_a_taken_initiative(taken_initiative_id: int, db: Session = Depends(get_session)):
    return read_taken_initiative(taken_initiative_id=taken_initiative_id, db=db)

@router.delete("/{taken_initiative_id}")
def delete_a_taken_initiative(taken_initiative_id: int, db: Session = Depends(get_session)):
    return delete_taken_initiative(taken_initiative_id=taken_initiative_id, db=db)
