from src.tools.base import BaseTool
from src.database.models import NoteModel
from src.database.session import async_session
from sqlalchemy.future import select
from typing import List, Dict, Any

class NotesTool(BaseTool):
    """
    Tool for managing personal notes.
    Provides save, search, and delete operations.
    """
    def __init__(self):
        super().__init__("NotesTool")

    async def save_note(self, title: str, content: str) -> Dict[str, Any]:
        """Saves a new note."""
        async with async_session() as session:
            note = NoteModel(title=title, content=content)
            session.add(note)
            await session.commit()
            return {"id": note.id, "title": note.title, "status": "saved"}

    async def search_notes(self, query: str) -> List[Dict[str, Any]]:
        """Searches notes by title and content (case-insensitive)."""
        async with async_session() as session:
            q = f"%{query}%"
            result = await session.execute(
                select(NoteModel).filter(
                    (NoteModel.title.ilike(q)) | (NoteModel.content.ilike(q))
                )
            )
            notes = result.scalars().all()
            return [{"id": n.id, "title": n.title, "content": n.content} for n in notes]

    async def delete_note(self, note_id: int) -> Dict[str, Any]:
        """Deletes a note."""
        async with async_session() as session:
            result = await session.execute(select(NoteModel).filter_by(id=note_id))
            note = result.scalar_one_or_none()
            if note:
                await session.delete(note)
                await session.commit()
                return {"id": note_id, "status": "deleted"}
            return {"error": "Note not found"}
