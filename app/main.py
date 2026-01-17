from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes import ingest, patterns_api, reflect, intervene, persona
from cognis.memory.vectorstore import load_vector_store
from cognis.memory.embeddings import get_embedding_model
import logging

# ✅ CONFIG LOGGING (FAANG Style)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("cognis")

app = FastAPI(
    title="Cognis API",
    description="FAANG-Level Cognitive Intelligence Engine",
    version="0.2"
)

@app.on_event("startup")
def startup():
    """
    Attempt to load memory and retriever on startup.
    """
    logger.info("🚀 Initializing Cognis Intelligence Engine...")
    
    embeddings = get_embedding_model()
    vector_store = load_vector_store(embeddings)
    
    if vector_store:
        app.state.vector_store = vector_store
        app.state.retriever = vector_store.as_retriever(search_kwargs={"k": 5})
        logger.info("🧠 Memory loaded successfully")
    else:
        app.state.vector_store = None
        app.state.retriever = None
        logger.warning("⚠️ No persistent memory found. Please ingest data first.")

# ✅ ROUTES
app.include_router(ingest.router, prefix="/ingest", tags=["Ingest"])
app.include_router(reflect.router, prefix="/reflect", tags=["Reflect"])
app.include_router(patterns_api.router, prefix="/patterns", tags=["Patterns"])
app.include_router(intervene.router, prefix="/intervene", tags=["Intervene"])
app.include_router(persona.router, prefix="/persona", tags=["Persona"])

# ✅ SERVE DASHBOARD
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def read_index():
    return FileResponse("app/static/index.html")
