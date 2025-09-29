import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

app = Flask(__name__)

PDF_PATH = "The_Constitution_of_Kenya_2010.pdf"

# ==============================
# SETUP
# ==============================
def build_qa_chain(pdf_path=PDF_PATH):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    llm = ChatGroq(
        model="llama-3.1-8b-instant",  # ✅ working Groq model
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY")
    )

    # Answers in numbered paragraphs
    template = """
    You are a helpful assistant that answers questions about the Constitution of Kenya (2010).
    Use the retrieved context below to answer the question.
    Format your answer in numbered paragraphs (1., 2., 3., …).
    
    Context:
    {context}

    Question:
    {question}

    Answer in numbered format:
    """
    qa_prompt = PromptTemplate.from_template(template)

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        chain_type="stuff",
        chain_type_kwargs={"prompt": qa_prompt}
    )
    return qa

qa_chain = build_qa_chain()

# ==============================
# ROUTES
# ==============================
@app.route("/", methods=["GET", "POST"])
def index():
    question, answer = None, None
    if request.method == "POST":
        question = request.form["question"]
        answer = qa_chain.run(question)

    return render_template("chat.html", question=question, answer=answer)

# ==============================
# MAIN
# ==============================
if __name__ == "__main__":
    if not os.getenv("GROQ_API_KEY"):
        raise ValueError("Please set GROQ_API_KEY in your .env file.")
    app.run()