from fastapi import FastAPI
from app.routes import ingest, patterns_api, reflect, intervene


# ✅ CREATE APP FIRST
app = FastAPI(
    title="Cognis API",
    description="Cognitive Pattern Detection & Intervention Engine",
    version="0.1"
)

# ✅ Minimal startup (NO embeddings)
@app.on_event("startup")
def startup():
    app.state.vector_store = None
    app.state.retriever = None
    print("🚀 Cognis API started (stateless mode)")


# ✅ ROUTES
app.include_router(ingest.router, prefix="/ingest", tags=["Ingest"])
app.include_router(reflect.router, prefix="/reflect", tags=["Reflect"])
app.include_router(patterns_api.router, prefix="/patterns", tags=["Patterns"])
app.include_router(intervene.router, prefix="/intervene", tags=["Intervene"])
