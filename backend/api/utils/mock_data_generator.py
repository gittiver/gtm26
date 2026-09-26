from sqlmodel import Session

from api.database import engine
from api.public.models import Proposal
from api.public.models import TakenInitiative

from api.utils.logger import logger_config

logger = logger_config(__name__)


def create_proposals_and_taken_initiatives():
    with Session(engine) as session:
        proposal_1 = Proposal(name="Save an Animal")
        proposal_2 = Proposal(name="Collect some Garbage")

        session.add(proposal_1)
        session.add(proposal_2)
        session.commit()

        session.refresh(proposal_1)
        session.refresh(proposal_2)

        t1 = TakenInitiative(proposal_id = proposal_1.id, location = None,comment = "comment1")
        t2 = TakenInitiative(proposal_id = proposal_2.id, location="Geist",comment="comment 2")

        session.add(t1)
        session.add(t2)
        session.commit()

        session.refresh(t1)
        session.refresh(t2)

        logger.info("=========== MOCK DATA CREATED ===========")
        logger.info("p1 %s", proposal_1)
        logger.info("p2 %s", proposal_2)
        logger.info("t1 %s", t1)
        logger.info("t2 %s", t2)
        logger.info("===========================================")
