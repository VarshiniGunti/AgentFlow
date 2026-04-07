# AgentFlow

AgentFlow is a multi-agent AI productivity assistant that coordinates specialized AI agents to manage tasks, schedules, and notes through automated workflows.

## Live Demo

**Frontend UI:**
[https://agentflow-88256365321.us-central1.run.app/](https://agentflow-88256365321.us-central1.run.app/)

**API Docs:**
[https://agentflow-88256365321.us-central1.run.app/docs](https://agentflow-88256365321.us-central1.run.app/docs)

## Problem Statement

**Multi-Agent Productivity Assistant**
Build a multi-agent AI system that helps users manage tasks, schedules, and information by interacting with multiple tools and data sources.

**Core Requirements:**

- Implement a primary coordinating agent
- Store and retrieve structured data from a database
- Integrate multiple tools via MCP (e.g., calendar, task manager, notes)
- Handle multi-step workflows and task execution
- Deploy as an API-based system

## Solution Overview

AgentFlow utilizes a hierarchical multi-agent architecture where a central orchestrator delegates steps to specialized local agents.

**Architectural Flow:**
User Prompt → PlannerAgent (Gemini) → OrchestratorAgent → Specialized Agents → Tools → Database

**Example Workflow:**
*PlannerAgent* decomposes the user prompt → *CalendarAgent* schedules the meeting → *TaskAgent* adds preparation steps to the to-do list.

## Key Features

- Multi-agent coordination
- MCP tool integration
- Multi-step workflow automation
- SQLite structured storage
- Glassmorphism UI with workflow visualization

## Architecture

```text
frontend/            # Glassmorphism UI and SVG Visualizations
src/
  agents/            # Logic for Planner, Orchestrator, Task, Calendar, Note agents
  tools/             # Tools mapping to specialized agents
  database/          # SQLAlchemy async session management
  api/               # FastAPI endpoints and MCP Server
  utils/             # Schemas, Prompts, and Logging
```

## Technology Stack

- **Backend**: Python, FastAPI, SQLAlchemy
- **AI**: Google Gemini
- **Frontend**: HTML, TailwindCSS (Native CSS constraints)
- **Protocol**: MCP (Model Context Protocol)
- **Deployment**: Google Cloud Run

## How It Works

1. **User Prompt**: The user submits a natural language request via the frontend.
2. **Planner**: The `PlannerAgent` decomposes the prompt into a JSON plan of sequential tools.
3. **Orchestrator**: The `OrchestratorAgent` registers and triggers the required Specialized Agents.
4. **Agents & Tools**: `Task`, `Calendar`, and `Notes` agents execute tool logic (like MCP endpoints).
5. **Database**: Persistent storage occurs via `aiosqlite`. Data is saved and verified.

## API Example

**Request:** `POST /query`

```json
{
 "prompt": "Schedule a meeting tomorrow and create tasks to prepare slides"
}
```

**Response Example:**

```json
{
  "workflow": [
    "planner.create_plan",
    "calendar.create_event",
    "task.create_task"
  ],
  "results": {
    "calendar_event": "Meeting scheduled for 2026-04-08T10:00:00",
    "task_created": "Task #1: Prepare slides"
  },
  "plan_rationale": "Orchestrating a strategic event while synchronizing with deep memory context."
}
```

## Running Locally

Clone the repository and install dependencies:

```bash
git clone https://github.com/VarshiniGunti/AgentFlow
cd AgentFlow
pip install -r requirements.txt
cp .env.example .env
```

Add your `GEMINI_API_KEY` to the `.env` file, then run:

```bash
python -m src.api.main
```

Open your browser to:
`http://localhost:8000`

## MCP Server

AgentFlow runs an official MCP compliant server. To launch it standalone:

```bash
python -m src.api.mcp_server
```

## Evaluation Criteria Coverage

- **Solution Quality & Functionality (20%)**: Handled via robust state mapping and error handling between the Planner and Sub-agents.
- **Architecture & Technical Execution (20%)**: Employs scalable `asyncio` and `aiosqlite` execution for non-blocking processes.
- **Impact & Use Case Relevance (20%)**: Tackles context-switching by merging scheduling, tasks, and notes organically.
- **Technical Choices & Feasibility (20%)**: Leverages the Model Context Protocol (MCP) standardization natively.
- **Demo, UX & Presentation (20%)**: Implements an elite "Neural Swarm" Glassmorphism UI with real-time process monitoring.

## Author

**Varshini Gunti** – IIT Bhilai
