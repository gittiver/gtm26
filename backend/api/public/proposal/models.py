from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel
from api.public.models import ProposalBase

class ProposalCreate(ProposalBase):
    pass


class ProposalRead(ProposalBase):
    id: int


class ProposalUpdate(ProposalBase):
    pass