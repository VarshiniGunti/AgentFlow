from src.agents.base import BaseAgent
from src.tools.calendar_tool import CalendarTool
from src.utils.schemas import Action
from typing import Any

class CalendarAgent(BaseAgent):
    """
    Agent responsible for managing calendar events.
    Uses CalendarTool to interact with the database.
    """
    def __init__(self):
        super().__init__("CalendarAgent", "Schedule and manage calendar events")
        self.tool = CalendarTool()
        self.tools = {
            "create_event": self.tool.create_event,
            "list_events": self.tool.list_events,
            "delete_event": self.tool.delete_event
        }

    async def execute(self, action: Action) -> Any:
        tool_name = action.tool
        params = action.params
        
        self.logger.info("executing_tool", tool=tool_name, params=params)
        
        if tool_name not in self.tools:
            raise ValueError(f"Unknown tool: {tool_name} for {self.name}")
            
        tool_function = self.tools[tool_name]
        return await tool_function(**params)
