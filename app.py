from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rag import load_rag_pipeline

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

qa_chain = load_rag_pipeline()

@app.post("/ask")
async def ask(request: Request):
    body = await request.json()
    pregunta = body.get("pregunta", "")
    respuesta = qa_chain.run(pregunta)
    return {"respuesta": respuesta}
