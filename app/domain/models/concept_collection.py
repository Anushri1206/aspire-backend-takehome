from typing import Optional
from sqlmodel import Field, SQLModel


class ConceptCollectionBase(SQLModel):
    label: str = Field(max_length=255)
    content_summary: Optional[str] = None


class ConceptCollection(ConceptCollectionBase, table=True):
    __tablename__ = "concept_collection"
    id: Optional[int] = Field(default=None, primary_key=True)


class CollectionRead(ConceptCollection):
    pass

class CollectionUpdate(SQLModel):
    title: Optional[str] = None
    content_summary: Optional[str] = None

