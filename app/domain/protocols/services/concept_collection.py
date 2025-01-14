from typing import Protocol

from app.domain.models.concept_collection import CollectionRead, CollectionUpdate



class CollectionService(Protocol):
    """
    Services related to ConceptCollections
    """
    async def update_collection(self, collection_id: int, collection_update: CollectionUpdate) -> CollectionRead:
        """
        Uses the set values of a CollectionUpdate obj to update the corresponding columns of a ConceptCollection entry where the provided collection_id matches the primary key.

        :param collection_id: The id of the ConceptCollection to update
        :param collection_update: A CollectionUpdate obj with set fields specifying the columns to update and the new values
        :return: CollectionRead
        :raises DBError: When the collection_id matches no collections or the update is invalid.
        """
        ...

