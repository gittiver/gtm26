from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select

from api.database import get_session
from api.public.models import TakenInitiative
from api.public.took_initiative.models import TakenInitiativeCreate

def create_taken_initiative (taken_initiative : TakenInitiativeCreate, db: Session = Depends(get_session)):
    taken_initiative_to_db = TakenInitiative .model_validate(taken_initiative )
    db.add(taken_initiative_to_db)
    db.commit()
    db.refresh(taken_initiative_to_db)
    return taken_initiative_to_db

def read_taken_initiatives(offset: int = 0, limit: int = 20, db: Session = Depends(get_session)):
    taken_initiatives = db.exec(select(TakenInitiative ).offset(offset).limit(limit)).all()
    return taken_initiatives


def read_taken_initiative (taken_initiative_id: int, db: Session = Depends(get_session)):
    taken_initiative  = db.get(TakenInitiative , taken_initiative_id)
    if not taken_initiative :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"TakenInitiative  not found with id: {taken_initiative_id}",
        )
    return taken_initiative

def delete_taken_initiative (taken_initiative_id: int, db: Session = Depends(get_session)):
    taken_initiative  = db.get(TakenInitiative , taken_initiative_id)
    if not taken_initiative :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"TakenInitiative  not found with id: {taken_initiative_id}",
        )

    db.delete(taken_initiative )
    db.commit()
    return {"ok": True}
