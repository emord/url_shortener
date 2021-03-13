from pydantic import BaseModel


class LinkBase(BaseModel):
    url: str


class LinkCreate(LinkBase):
    pass


class Link(LinkBase):
    id: int
    method: str
    shortened: str

    class Config:
        orm_mode = True
