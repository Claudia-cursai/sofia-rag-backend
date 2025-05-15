from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

@app.post("/ask")
async def ask(request: Request):
    body = await request.json()
    pregunta = body.get("pregunta", "").lower()
    respuesta = ""

    for zona in data:
        if zona["nombre"].lower() in pregunta:
            respuesta = zona["descripcion"]
            break

    return {"respuesta": respuesta or "No estoy seguro, ¿podés aclararme un poco más?"}
