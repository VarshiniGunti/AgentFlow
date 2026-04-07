from fastapi import FastAPI
from fastapi.responses import FileResponse
from src.api.routes import router
from src.database.session import init_db
from src.utils.logger import logger
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="AgentFlow API", description="Multi-Agent System for Tasks, Calendar, and Notes")

@app.on_event("startup")
async def on_startup():
    """Operations to perform on application startup."""
    logger.info("application_startup")
    await init_db()

app.include_router(router)

# Serve static files
frontend_path = os.path.join(os.getcwd(), "frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/")
async def root():
    """Serve the frontend index.html."""
    index_path = os.path.join(frontend_path, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "AgentFlow Multi-Agent System is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
