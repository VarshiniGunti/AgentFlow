# 🧠 AgentFlow: Neural Orchestrator

---

## 🎯 Problem Statement

**Challenge**: *Build a multi-agent AI system that helps users manage tasks, schedules, and information by interacting with multiple tools and data sources. Ensure it stores and retrieves structured data, integrates tools via MCP, handles multi-step workflows, and deploys as an API-based system.*

**Our Solution: AgentFlow**
AgentFlow goes beyond basic chatbot interfaces. It provides a true "Swarm Intelligence" architecture. It breaks down complex user goals into sequence dependencies, stores critical data in a persistent SQL database, and introduces real-time visual transparency to the AI process through its `Neural Atlas` UI.

---

## ✨ Key Features

1. **Neural Swarm Atlas**: A dynamic, process-centric SVG visualization that shows real-time "Data Packets" routing from the `Planner` to specialized sub-agents (`Task`, `Calendar`, `Notes`, `Research`).
2. **Deep Memory Link Protocol**: The Orchestrator automatically "sweeps" the user's historical notes for relevant context on *every* request, creating a proactive, highly personalized AI experience.
3. **Neural Reflection Telemetry**: A real-time, scrolling console feed displaying the raw thoughts and synchronization logs of the agent swarm.
4. **Voice-Native UX**: Full Web Speech integration for hands-free input (Speech-to-Task) and high-quality, localized US English voice narration (TTS) of AI rationales.
5. **Standardized Interoperability**: Built with a dedicated **Model Context Protocol (MCP)** server, allowing external clients and IDEs to plug into AgentFlow's tooling ecosystem natively.

---

## 🛠️ Tech Stack

* **Backend Application**: Python `FastAPI`, `Uvicorn`
* **Database ORM**: `SQLAlchemy` (Async) with `aiosqlite`
* **AI Engine**: `google-generativeai` (Gemini-Flash)
* **Protocol Standard**: Official `mcp` SDK implementation
* **Frontend**: Native HTML5, Vanilla JavaScript, and Advanced CSS Animations (Glassmorphism & SVG paths)
* **Deployment**: Fully containerized with Docker, optimized for Google Cloud Run.

---

## 🚀 Setup & Execution

### 1. Prerequisites

- Python 3.10+
* Google Gemini API Key

### 2. Installation

```bash
git clone https://github.com/VarshiniGunti/AgentFlow.git
cd AgentFlow
```

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configuration

Rename `.env.example` to `.env` and configure your API keys:

```env
GEMINI_API_KEY=your_actual_key_here
```

### 4. Run the System

**Start the Primary API Backend & UI**:

```bash
python -m src.api.main
```

*Access the Elite UI at: `http://localhost:8000`*
*Access API Specs at: `http://localhost:8000/docs`*

**Start the Standalone MCP Server**:

```bash
python -m src.api.mcp_server
```

---

## 🏗️ Architecture

AgentFlow uses a hierarchical multi-agent structure:

* **OrchestratorAgent**: The entry point that manages the communication flow.
* **PlannerAgent**: Equipped with LLM capabilities. It decomposes high-level user prompts into structured JSON action plans.
* **Specialized Sub-Agents**: Directly manipulate the database layer.
  * **TaskAgent**: Manages to-do lists.
  * **CalendarAgent**: Handles meetings and timestamps.
  * **NotesAgent**: Captures and semantic-searches persistent knowledge base.
  * **ResearchAgent**: Gathers external context.

## 🤝 Model Context Protocol (MCP) Integration

AgentFlow is built for the future of AI. It natively exposes a `StdioServerTransport` for MCP clients. This means AgentFlow tools (`create_task`, `create_event`, `save_note`) can be instantly utilized by external MCP-compliant LLMs (like Claude Desktop) as a powerful backend provider.

---
*Created for Hackathon Excellence. 🏆*
