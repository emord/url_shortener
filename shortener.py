 # pylint: disable=no-name-in-module
import hashlib

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic.main import BaseModel
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/l/{link}")
def link(link, db: Session = Depends(get_db)):
    db_link = crud.get_link_from_shortened(db, link)
    if not db_link:
        return HTTPException(404, "not found")
    crud.record_access(db, db_link)
    return RedirectResponse(db_link.url)

@app.post("/shorten", response_model=schemas.Link)
def shorten(link: schemas.LinkCreate, db: Session = Depends(get_db)):
    db_link = crud.get_link_by_url(db, link.url)
    if db_link:
        return db_link
    return crud.create_shortened(db=db, link=link)
