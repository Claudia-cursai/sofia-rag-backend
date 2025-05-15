from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rag import load_rag_pipeline
import embedder  # ⚠️ Esto se puede eliminar luego de correr una vez

app = FastAPI()

# Permite solicitudes desde cualquier origen (ideal si usás front externo o pruebas locales)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

qa_chain = load_rag_pipeline()

@app.post("/ask")
async def ask(request: Request):
    body = await request.json()
    pregunta = body.get("pregunta", "")
    respuesta = qa_chain.run(pregunta)
    return {"respuesta": respuesta}

@app.get("/")
def read_root():
    return {"mensaje": "Backend activo"}
