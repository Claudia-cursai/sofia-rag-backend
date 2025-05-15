from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rag import load_rag_pipeline

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

qa_chain = None  # No se carga al inicio

@app.post("/ask")
async def ask(request: Request):
    global qa_chain
    if qa_chain is None:
        qa_chain = load_rag_pipeline()  # Se carga solo cuando llega la primera pregunta

    body = await request.json()
    pregunta = body.get("pregunta", "")
    respuesta = qa_chain.run(pregunta)
    return {"respuesta": respuesta}
