from src.tools.base import BaseTool
from src.database.models import EventModel
from src.database.session import async_session
from sqlalchemy.future import select
from datetime import datetime
from typing import List, Dict, Any

class CalendarTool(BaseTool):
    """
    Tool for managing calendar events.
    Provides create, list, and delete operations.
    """
    def __init__(self):
        super().__init__("CalendarTool")

    async def create_event(self, title: str, start_time: str, location: str = None) -> Dict[str, Any]:
        """Creates a new event. start_time should be ISO format string."""
        async with async_session() as session:
            dt = datetime.fromisoformat(start_time)
            event = EventModel(title=title, start_time=dt, location=location)
            session.add(event)
            await session.commit()
            return {"id": event.id, "title": event.title, "start_time": start_time}

    async def list_events(self) -> List[Dict[str, Any]]:
        """Lists all calendar events."""
        async with async_session() as session:
            result = await session.execute(select(EventModel))
            events = result.scalars().all()
            return [{"id": e.id, "title": e.title, "start_time": e.start_time.isoformat()} for e in events]

    async def delete_event(self, event_id: int) -> Dict[str, Any]:
        """Deletes an event from the calendar."""
        async with async_session() as session:
            result = await session.execute(select(EventModel).filter_by(id=event_id))
            event = result.scalar_one_or_none()
            if event:
                await session.delete(event)
                await session.commit()
                return {"id": event_id, "status": "deleted"}
            return {"error": "Event not found"}
