import hashlib

from sqlalchemy.orm import Session

import models, schemas


def get_link_by_url(db: Session, url: str):
    return db.query(models.Link).filter(models.Link.url == url).first()


def get_link_from_shortened(db: Session, shortened: str):
    return (
        db.query(models.Link)
        .filter(models.Link.shortened.startswith(shortened))
        .first()
    )


def create_shortened(db: Session, link: schemas.LinkCreate):
    shortened = hashlib.sha256(link.url.encode("utf-8")).hexdigest()
    db_link = models.Link(url=link.url, shortened=shortened, method="sha256")
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link


def record_access(db: Session, link: schemas.Link):
    db.add(models.Access(link_id=link.id))
    db.commit()
