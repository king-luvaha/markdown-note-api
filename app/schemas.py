from pydantic import BaseModel

class NoteCreate(BaseModel):
    title: str

class NoteOut(BaseModel):
    id: int
    title: str
    content: str
    html_content: str
    grammar_issues: str

    class Config:
        from_attributes = True  # use this for Pydantic v2+
