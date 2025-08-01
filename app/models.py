from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    content = Column(Text)
    html_content = Column(Text)
    grammar_issues = Column(Text)
