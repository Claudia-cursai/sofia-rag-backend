from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

def load_rag_pipeline():
    print("🧠 Intentando cargar el vectorstore...")

    # Verifica que el archivo FAISS exista
    if not os.path.exists("vectorstore/index.faiss"):
        print("❌ No se encontró el vectorstore. Ejecutá 'python embedder.py' desde la consola para crearlo.")
        raise FileNotFoundError("Falta el vectorstore. Ejecutá 'python embedder.py' desde la consola.")

    # Si existe, continúa con la carga normal
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local("vectorstore", embeddings)
    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    print("✅ Vectorstore cargado correctamente.")
    return qa_chain

