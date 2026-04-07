import asyncio
from mcp.server.fastmcp import FastMCP
from src.tools.task_tool import TaskTool
from src.tools.calendar_tool import CalendarTool
from src.tools.notes_tool import NotesTool
from src.utils.logger import logger

# Initialize FastMCP server
mcp = FastMCP("AgentFlow")

# Initialize tools
task_tool = TaskTool()
calendar_tool = CalendarTool()
notes_tool = NotesTool()

@mcp.tool()
async def create_task(title: str, description: str = None) -> str:
    """
    Creates a new task in AgentFlow.
    
    Args:
        title: The title of the task.
        description: Optional description of the task.
    """
    logger.info("mcp_tool_call", tool="create_task", title=title)
    result = await task_tool.create_task(title, description)
    return str(result)

@mcp.tool()
async def create_event(title: str, start_time: str, location: str = "Remote") -> str:
    """
    Schedules a new event in the AgentFlow calendar.
    
    Args:
        title: The title of the meeting or event.
        start_time: ISO 8601 formatted string (YYYY-MM-DDTHH:MM:SS)
        location: Where the event is held.
    """
    logger.info("mcp_tool_call", tool="create_event", title=title)
    result = await calendar_tool.create_event(title, start_time, location)
    return str(result)

@mcp.tool()
async def save_note(title: str, content: str) -> str:
    """
    Saves a persistent note in AgentFlow.
    
    Args:
        title: The title of the note.
        content: The body text of the note.
    """
    logger.info("mcp_tool_call", tool="save_note", title=title)
    result = await notes_tool.save_note(title, content)
    return str(result)

if __name__ == "__main__":
    # Start the MCP server using stdio transport
    mcp.run()
