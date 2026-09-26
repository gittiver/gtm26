from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select

from api.database import get_session
from api.public.models import Proposal 
from api.public.proposal.models import ProposalCreate, ProposalUpdate


def create_proposal (proposal : ProposalCreate, db: Session = Depends(get_session)):
    proposal_to_db = Proposal .model_validate(proposal )
    db.add(proposal_to_db)
    db.commit()
    db.refresh(proposal_to_db)
    return proposal_to_db

def read_proposals(offset: int = 0, limit: int = 20, db: Session = Depends(get_session)):
    proposals = db.exec(select(Proposal ).offset(offset).limit(limit)).all()
    return proposals


def read_proposal (proposal_id: int, db: Session = Depends(get_session)):
    proposal  = db.get(Proposal , proposal_id)
    if not proposal :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Proposal  not found with id: {proposal_id}",
        )
    return proposal 

def update_proposal (proposal_id: int, proposal : ProposalUpdate, db: Session = Depends(get_session)):
    proposal_to_update = db.get(Proposal , proposal_id)
    if not proposal_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Proposal  not found with id: {proposal_id}",
        )

    team_data = proposal .model_dump(exclude_unset=True)
    for key, value in team_data.items():
        setattr(proposal_to_update, key, value)

    db.add(proposal_to_update)
    db.commit()
    db.refresh(proposal_to_update)
    return proposal_to_update


def delete_proposal (proposal_id: int, db: Session = Depends(get_session)):
    proposal  = db.get(Proposal , proposal_id)
    if not proposal :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Proposal  not found with id: {proposal_id}",
        )

    db.delete(proposal )
    db.commit()
    return {"ok": True}
