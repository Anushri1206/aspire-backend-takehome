import logging
import json
from typing import Any, Dict, Iterable

from sqlmodel import SQLModel, Session
from app.domain.models.concept import Concept, ConceptToCollection, ConceptToConcept
from app.domain.models.concept_collection import ConceptCollection

logger = logging.getLogger(__name__)

# TODO implement your own data seeding or remove this code.

def _populate_table(
    db: Session, table: SQLModel, values: Iterable[Dict[str, Any]],
):
    name = table.__tablename__
    logger.info(f"Seeding table {name}")
    for v in values:
        try:
            db.add(table.from_orm(v))
            db.commit()
        except Exception as e:
            # To ignore Duplicate Violation errors
            continue
    db.close_all()
    logger.info(f"Seeded table {name} successfully")

def _populate_db(db: Session):
    ordered_table_lookup = {
        "concept": Concept,
        "concept_collection": ConceptCollection,
        "concept_to_concept": ConceptToConcept,
        "concept_to_collection": ConceptToCollection
    }

    with open("app/infrastructure/seed.json", "r") as file:
        db_seed = json.load(file)
        for name, table in ordered_table_lookup.items():
            _populate_table(db=db, table=table, values=db_seed.get(name))


def run(db: Session) -> None:
    logger.info("Initializing databases")
    logger.info("Populating database")
    for fn in [_populate_db]:
        fn(db)
    logger.info("Finished populating database")