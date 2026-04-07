from src.agents.base import BaseAgent
from src.tools.task_tool import TaskTool
from src.utils.schemas import Action
from typing import Any

class TaskAgent(BaseAgent):
    """
    Agent responsible for managing tasks.
    Uses TaskTool to interact with the database.
    """
    def __init__(self):
        super().__init__("TaskAgent", "Manage user To-Do lists and tasks")
        self.tool = TaskTool()
        self.tools = {
            "create_task": self.tool.create_task,
            "list_tasks": self.tool.list_tasks,
            "complete_task": self.tool.complete_task
        }

    async def execute(self, action: Action) -> Any:
        tool_name = action.tool
        params = action.params
        
        self.logger.info("executing_tool", tool=tool_name, params=params)
        
        if tool_name not in self.tools:
            raise ValueError(f"Unknown tool: {tool_name} for {self.name}")
            
        tool_function = self.tools[tool_name]
        return await tool_function(**params)
