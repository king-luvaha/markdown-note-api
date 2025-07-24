from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
import os

from . import database, models, crud, utils, schemas

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/", response_model=schemas.NoteOut)
async def upload_note(
    title: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not file.filename.endswith(".md"):
        raise HTTPException(status_code=400, detail="Only markdown files are allowed")
    
    content = (await file.read()).decode("utf-8")
    html = utils.convert_md_to_html(content)
    grammar = utils.check_grammar(content)

    note = crud.create_note(db, title=title, content=content, html=html, grammar=grammar)
    return note

@app.get("/notes/", response_model=list[schemas.NoteOut])
def list_notes(db: Session = Depends(get_db)):
    return crud.get_notes(db)

@app.get("/notes/{note_id}", response_model=schemas.NoteOut)
def get_single_note(note_id: int, db: Session = Depends(get_db)):
    note = crud.get_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note
