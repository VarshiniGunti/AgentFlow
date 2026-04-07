import os
from src.agents.base import BaseAgent
from src.utils.schemas import Action
from typing import Any
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class ResearchAgent(BaseAgent):
    """
    Agent that simulates external research using the Gemini LLM.
    """
    def __init__(self):
        super().__init__("ResearchAgent", "Perform simulated external research or fact-gathering")
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-flash-latest')
        else:
            self.model = None

    async def execute(self, action: Action) -> Any:
        if action.tool == "research_topic":
            query = action.params.get("query", "")
            return await self.research_topic(query)
        return {"error": f"Tool '{action.tool}' not supported by ResearchAgent"}

    async def research_topic(self, query: str) -> str:
        if not self.model:
            return f"[Simulated Search] Researching: {query}. (API Key missing for realistic simulation)"

        prompt = f"""
        You are a Research Assistant for AgentFlow.
        The user wants to research: '{query}'
        
        Provide a concise, factual, and helpful synthesis of information related to this topic. 
        Format it as a bulleted list of 3-5 key points.
        Include a 'Source Simulation' at the end (e.g. 'Synthesized from curated knowledge bases').
        """
        
        try:
            response = await self.model.generate_content_async(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error performing research: {str(e)}"
