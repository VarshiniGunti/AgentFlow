from abc import ABC
from src.utils.logger import logger

class BaseTool(ABC):
    """
    Abstract Base Class for all tools in AgentFlow.
    Tools provide the interface for agents to interact with underlying data or external services.
    """
    def __init__(self, name: str):
        self.name = name
        self.logger = logger.bind(tool_name=name)
