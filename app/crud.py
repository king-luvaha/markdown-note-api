from sqlalchemy.orm import Session
from . import models

def create_note(db: Session, title: str, content: str, html: str, grammar: str):
    note = models.Note(title=title, content=content, html_content=html, grammar_issues=grammar)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def get_notes(db: Session):
    return db.query(models.Note).all()

def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()
