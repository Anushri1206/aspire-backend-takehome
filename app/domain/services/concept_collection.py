from fastapi import Depends

from app.domain.protocols.repositories.concept_collection import CollectionRepository as CollectionRepoProtocol
from app.domain.protocols.services.concept_collection import CollectionService as CollectionServiceProtocol

from app.infrastructure.repositories.concept_collection import CollectionRepository
from app.domain.models.concept_collection import CollectionRead, CollectionUpdate



class CollectionService(CollectionServiceProtocol):
    def __init__(
            self, 
            collection_repo: CollectionRepoProtocol = Depends(CollectionRepository)
    ):
        self.collection_repo = collection_repo

    async def update_collection(self, collection_id: int, collection_update: CollectionUpdate) -> CollectionRead:
        return await self.collection_repo.update(collection_id=collection_id, collection_update=collection_update)
