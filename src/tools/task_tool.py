from src.tools.base import BaseTool
from src.database.models import TaskModel
from src.database.session import async_session
from sqlalchemy.future import select
from typing import List, Dict, Any

class TaskTool(BaseTool):
    """
    Tool for managing tasks in the database.
    Provides create, list, and complete operations.
    """
    def __init__(self):
        super().__init__("TaskTool")

    async def create_task(self, title: str, description: str = None) -> Dict[str, Any]:
        """Creates a new task."""
        async with async_session() as session:
            task = TaskModel(title=title, description=description)
            session.add(task)
            await session.commit()
            return {"id": task.id, "title": task.title, "status": "created"}

    async def list_tasks(self) -> List[Dict[str, Any]]:
        """Lists all tasks."""
        async with async_session() as session:
            result = await session.execute(select(TaskModel))
            tasks = result.scalars().all()
            return [{"id": t.id, "title": t.title, "completed": t.is_completed} for t in tasks]

    async def complete_task(self, task_id: int) -> Dict[str, Any]:
        """Marks a task as completed."""
        async with async_session() as session:
            result = await session.execute(select(TaskModel).filter_by(id=task_id))
            task = result.scalar_one_or_none()
            if task:
                task.is_completed = True
                await session.commit()
                return {"id": task_id, "status": "completed"}
            return {"error": "Task not found"}
