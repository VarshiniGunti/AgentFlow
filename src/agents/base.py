from abc import ABC, abstractmethod
from typing import Any, List
from src.utils.logger import logger
from src.utils.schemas import Action

class BaseAgent(ABC):
    """
    Abstract Base Class for all agents in the AgentFlow system.
    Each agent must implement the execute method to handle specific actions.
    """
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.logger = logger.bind(agent_name=name, agent_role=role)

    @abstractmethod
    async def execute(self, action: Action) -> Any:
        """
        Executes a structured action using the agent's tools.
        
        Args:
            action (Action): The action to perform.
            
        Returns:
            Any: The result of the action execution.
        """
        pass
