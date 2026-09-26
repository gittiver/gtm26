from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from api.database import get_session
from api.public.proposal.crud import (
    create_proposal,
    delete_proposal,
    read_proposal,
    read_proposals,
    update_proposal,
)
from api.public.proposal.models import ProposalCreate, ProposalRead, ProposalUpdate

router = APIRouter()


@router.post("", response_model=ProposalRead)
def create_a_proposal(proposal: ProposalCreate, db: Session = Depends(get_session)):
    return create_proposal(proposal=proposal, db=db)


@router.get("", response_model=list[ProposalRead])
def get_proposals(
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    db: Session = Depends(get_session),
):
    return read_proposals(offset=offset, limit=limit, db=db)


@router.get("/{proposal_id}", response_model=ProposalRead)
def get_a_proposal(proposal_id: int, db: Session = Depends(get_session)):
    return read_proposal(proposal_id=proposal_id, db=db)


@router.patch("/{proposal_id}", response_model=ProposalRead)
def update_a_proposal(proposal_id: int, proposal: ProposalUpdate, db: Session = Depends(get_session)):
    return update_proposal(proposal_id=proposal_id, proposal=proposal, db=db)


@router.delete("/{proposal_id}")
def delete_a_proposal(proposal_id: int, db: Session = Depends(get_session)):
    return delete_proposal(proposal_id=proposal_id, db=db)
