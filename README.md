# AgentFlow

AgentFlow is a production-ready, asynchronous multi-agent system designed to manage tasks, schedules, and notes seamlessly. It leverages the power of Gemini (PlannerAgent) and specialized agents (Task, Calendar, Notes) to orchestrate complex workflows through a unified interface.

## Architecture

AgentFlow uses a hierarchical multi-agent architecture:

- **OrchestratorAgent**: The entry point that manages the communication flow.
- **PlannerAgent (Gemini)**: Decomposes high-level user prompts into actionable steps.
- **Specialized Agents**:
  - **TaskAgent**: Manages to-do lists and task tracking.
  - **CalendarAgent**: Handles meeting scheduling and event management.
  - **NotesAgent**: Captures and retrieves persistent notes.
- **Tools**: Direct interaction with a SQLite database via SQLAlchemy.

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd AgentFlow
   ```

2. **Configure environment variables**:
   - Rename `.env.example` to `.env`.
   - Add your [Gemini API Key](https://aistudio.google.com/app/apikey):

     ```text
     GEMINI_API_KEY=your_actual_key_here
     ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database** (if not already present):
   AgentFlow automatically creates `agentflow.db` on the first run.

## How to Run Locally

### Backend (FastAPI)

Start the server using:

```bash
python -m src.api.main
```

The backend will be available at `http://localhost:8000`.
Swagger docs: `http://localhost:8000/docs`.

### Frontend

Open `frontend/index.html` in your browser. The UI allows you to send natural language queries to the agent system.

## API Usage

- **POST /query**
  - **Payload**: `{"prompt": "string"}`
  - **Example Query**:

    ```json
    {
      "prompt": "Schedule a meeting tomorrow and create tasks to prepare slides"
    }
    ```

## MCP Tool Integration

AgentFlow is compliant with the **Model Context Protocol (MCP)**. It exposes its core tools as an MCP-compliant server, allowing external AI agents, IDEs, and other MCP clients to interact with the AgentFlow ecosystem directly.

### Running the MCP Server

Start the standalone MCP server using:

```bash
python -m src.api.mcp_server
```

### Exposed MCP Tools

- **`create_task(title, description)`**: Create and persist a new task.
- **`create_event(title, start_time, location)`**: Schedule a calendar event.
- **`save_note(title, content)`**: Save a new persistent note.

This allows AgentFlow to be used as a backend "tool provider" for any external agent system.

## Example Workflow

1. **User**: "Plan a marketing meeting for Friday at 10 AM and add 'Review budget' to my tasks."
2. **Planner**: Identifies two actions: `CalendarTool (add_event)` and `TaskTool (add_task)`.
3. **Orchestrator**: Dispatches to CalendarAgent and TaskAgent.
4. **Result**: Meeting scheduled, task created, and a summary returned to the user.
