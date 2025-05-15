from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def load_rag_pipeline():
    vectorstore = FAISS.load_local("vectorstore", OpenAIEmbeddings())
    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
