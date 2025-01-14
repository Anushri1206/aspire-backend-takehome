import logging
from typing import Union, Literal
from sqlmodel import Session, select
from sqlalchemy.exc import NoResultFound

from app.infrastructure.db import get_db

from app.errors.db_error import DBError

from app.domain.models.concept import (
    Concept,
    ConceptRead, 
    ConceptReadVerbose
    )

from app.domain.protocols.repositories.concept import ConceptRepository as ConceptRepositoryProtocol

logger = logging.getLogger(__name__)

class ConceptRepository(ConceptRepositoryProtocol):
    db: Session

    def __init__(self):
        self.db = get_db()


    async def get_one(self, concept: ConceptRead, read_mode: Literal["normal", "verbose"] = "normal") -> Union[ConceptRead, ConceptReadVerbose]:
        try:
            query_stmt = select(Concept).where(Concept.name == concept.name)
            results = self.db.exec(statement=query_stmt)

        except Exception as e:
            logger.exception(msg="Failed to return concept object.")
            raise DBError(
                origin="ConceptToConceptRepository.get_one",
                type="QueryExecError",
                status_code=500,
                message="Failed to return concept object."
            ) from e  
        
        try:
            results = results.one()

        except NoResultFound as e:
            logger.exception(msg=f"No Concept entry found at name == {concept.name}")
            raise DBError(
                origin="ConceptToConceptRepository.get_one",
                type="NotFoundError",
                status_code=404,
                message=f"No Concept entry found at name == {concept.name}"
            ) from e   
        
        try:
            self.db.close()

            if read_mode == "normal":
                return ConceptRead.model_validate(results)
            
            else:
                return ConceptReadVerbose.model_validate(results)
            
        except Exception as e:
            logger.exception(msg="Could not return ConceptToConceptRepository.get_one results")
            raise DBError(
                origin="ConceptToConceptRepository.get_one",
                type="ReturnError",
                status_code=500,
                message="Failed to return"
            ) from e   
