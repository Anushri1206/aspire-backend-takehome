from fastapi import Depends

from app.domain.models.concept import (
    ConceptRead, 
    ConceptReadVerbose,
    )
from app.domain.protocols.repositories.concept import ConceptRepository as ConceptRepoProtocol

from app.domain.protocols.services.concept import ConceptService as ConceptServiceProtocol
from app.infrastructure.repositories.concept import ConceptRepository
    


class ConceptService(ConceptServiceProtocol):
    def __init__(
        self, 
        concept_repo: ConceptRepoProtocol = Depends(ConceptRepository),
    ):
        self.concept_repo = concept_repo

    async def get_concept(self, concept: ConceptRead) -> ConceptReadVerbose:
        return await self.concept_repo.get_one(concept=concept, read_mode="verbose")
