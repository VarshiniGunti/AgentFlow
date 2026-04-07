from src.agents.base import BaseAgent
from src.tools.notes_tool import NotesTool
from src.utils.schemas import Action
from typing import Any

class NotesAgent(BaseAgent):
    """
    Agent responsible for managing personal notes.
    Uses NotesTool to interact with the database.
    """
    def __init__(self):
        super().__init__("NotesAgent", "Capture and search personal notes")
        self.tool = NotesTool()
        self.tools = {
            "save_note": self.tool.save_note,
            "search_notes": self.tool.search_notes,
            "delete_note": self.tool.delete_note
        }

    async def execute(self, action: Action) -> Any:
        tool_name = action.tool
        params = action.params
        
        self.logger.info("executing_tool", tool=tool_name, params=params)
        
        if tool_name not in self.tools:
            raise ValueError(f"Unknown tool: {tool_name} for {self.name}")
            
        tool_function = self.tools[tool_name]
        return await tool_function(**params)
