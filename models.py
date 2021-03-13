from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship

from database import Base

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True, nullable=False)
    shortened = Column(String, nullable=False)
    method = Column(String, nullable=False)


class Access(Base):
    __tablename__ = "accesses"

    id = Column(Integer, primary_key=True, index=True)
    link_id = Column(Integer, ForeignKey("links.id"), index=True, nullable=False)
    datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
