import json
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

documents = [
    Document(page_content=zona["descripcion"], metadata={"nombre": zona["nombre"]})
    for zona in data
]

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings)
vectorstore.save_local("vectorstore")
