from sqlmodel import Field, Relationship, SQLModel
from typing import List, Optional

from sqlmodel import Column, Field, Relationship, TIMESTAMP, SQLModel, text
from datetime import datetime

class ProposalBase(SQLModel):
    name: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Super Man",
            }
        }

class Proposal(ProposalBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    taken_initiatives: List[TakenInitiative] | None = Relationship(back_populates="proposal")    

class TakenInitiativeBase(SQLModel):
    comment: str
    location: str | None

    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
        ))
    proposal_id: int | None = Field(default=None, foreign_key="proposal.id")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "comment": "I did it!",
                "location": "Geist",
                "proposal_id": 1,
                "created_at": "2026-02-20"
            }
        }

class TakenInitiative(TakenInitiativeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    proposal: Proposal | None = Relationship(back_populates="taken_initiatives")
