from typing import Protocol

from app.domain.models.concept import (
    ConceptRead, 
    ConceptReadVerbose,
)


class ConceptService(Protocol):
    """
    Services related to Concepts
    """
    async def get_concept(self, concept: ConceptRead) -> ConceptReadVerbose:
        """
        Retrieves all data of a Concept entry filtered by the concept_name primary key attached to a provided ConceptRead obj.

        ConceptRead used instead of a regular string in order to use built-in title-case validation.

        :param concept: A ConceptRead obj with concept_name == string name of the target concept
        :return: ConceptReadVerbose
        :raises DBError: When ConceptRead.concept_name matches no concepts.
        """
        ...
