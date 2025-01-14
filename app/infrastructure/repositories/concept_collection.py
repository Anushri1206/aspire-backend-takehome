import logging

from fastapi import Depends
from sqlmodel import Session

from app.infrastructure.db import get_db

from app.errors.db_error import DBError

from app.domain.protocols.repositories.concept_collection import CollectionRepository as CollectionRepoProtocol
from app.domain.models.concept_collection import CollectionRead, CollectionUpdate, ConceptCollection

logger = logging.getLogger(__name__)

class CollectionRepository(CollectionRepoProtocol):
    db: Session
    
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    async def update(self, collection_id: int, collection_update: CollectionUpdate) -> CollectionRead:
        try:
            collection = self.db.get(ConceptCollection, collection_id)
            collection.sqlmodel_update(collection_update.model_dump(exclude_unset=True))
            
        except AttributeError as e:
            logger.exception(msg=f"No Collection entry at id == {collection_id}")
            raise DBError(
                origin="CollectionRepository.update",
                type="NotFoundError",
                status_code=404,
                message=f"No Collection entry at id == {collection_id}"
            ) from e
    
        try:
            self.db.add(collection)
            self.db.commit()

        except Exception as e:
            logger.exception(msg="Failed to update Collection object.")
            raise DBError(
                origin="CollectionRepository.update",
                type="QueryExecError",
                status_code=500,
                message="Failed to update Collection object."
            ) from e
        
        try:
            self.db.refresh(collection)
            self.db.close()
            return CollectionRead.model_validate(collection)
        
        except Exception as e:
            logger.exception(msg="Failed to return updated Collection object.")
            raise DBError(
                origin="CollectionRepository.update",
                type="ReturnError",
                status_code=500,
                message="Failed to return updated Collection object."
            ) from e
    
