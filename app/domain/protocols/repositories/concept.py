from typing import Protocol, Literal, Union

from app.domain.models.concept import (
    ConceptRead, 
    ConceptReadVerbose
    )

class ConceptRepository(Protocol):
    """
    DB Interface for accessing the Concept table
    """
    async def get_one(self, concept: ConceptRead, read_mode: Literal["normal", "verbose"] = "normal") -> Union[ConceptRead, ConceptReadVerbose]:
        """
        Returns a single concept filtered by name, 
        use read_mode='normal' for checking if a concept exists in the db,
        use read_mode='verbose' to return the details of a concept.

        :param concept_name: the name of the concept as a string
        :param read_mode: ('normal', 'verbose') in 'normal' mode just returns the concept name (useful to check if the concept exists in the db), in 'verbose' mode returns all the details of the concept
        :returns: Union[ConceptRead, ConceptReadVerbose]
        :raises DBError: When ConceptRead.concept_name matches no concepts.
        """
        ...