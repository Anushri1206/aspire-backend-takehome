from typing import Union
from pathlib import Path
from fastapi import APIRouter, Response, Depends

from app.errors.db_error import DBError
from app.domain.models.errors import ErrorResponse

from app.domain.models.concept import ConceptRead, ConceptReadVerbose
from app.domain.services.concept import ConceptService
from app.domain.protocols.services.concept import ConceptService as ConceptServiceProtocol

from app.domain.models.concept_collection import CollectionRead, CollectionUpdate
from app.domain.protocols.services.concept_collection import CollectionService as CollectionServiceProtocol
from app.domain.services.concept_collection import CollectionService

router = APIRouter()

BASE_PATH = Path(__file__).parent.resolve()


@router.get("/concept", response_model=Union[ConceptReadVerbose, ErrorResponse])
async def get_concept_details(
    response: Response,
    concept_name: str,
    concept_service: ConceptServiceProtocol = Depends(ConceptService)
) -> Union[ConceptReadVerbose, ErrorResponse]:
    """
    Retrieves a concept by its case-independent name
    """
    try:
        return await concept_service.get_concept(concept=ConceptRead(name=concept_name))
    
    except DBError as e:
        response.status_code = e.status_code
        return ErrorResponse(
            code=e.status_code,
            type=e.type,
            message=e.message
        )


@router.put("/collection/summary")
async def update_collection_summary(
    response: Response,
    collection_id: int,
    summary: str,
    collection_service: CollectionServiceProtocol = Depends(CollectionService)
) -> Union[CollectionRead, ErrorResponse]:
    """
    Updates the content_summary of a collection
    """
    try:
        return await collection_service.update_collection(collection_id=collection_id, collection_update=CollectionUpdate(content_summary=summary))
    
    except DBError as e:
        response.status_code = e.status_code
        return ErrorResponse(
            code=e.status_code,
            type=e.type,
            message=e.message
        )