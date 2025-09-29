# Constitution of Kenya Chatbot

This project implements a **Question Answering Chatbot** that responds to user queries about the **Constitution of Kenya (2010)**. It uses **LangChain**, **Groq LLM**, and **Flask** to provide a simple web interface where users can type questions and receive AI-generated answers based on the constitution text.

---

## 📂 Project Files

### 1. `app.py`

This is the main backend application file built using **Flask**. It performs the following functions:

* Loads the Constitution of Kenya (2010) PDF.
* Splits the document into manageable chunks using LangChain's text splitter.
* Generates vector embeddings with **HuggingFace sentence transformers**.
* Stores embeddings in a **FAISS vector database** for efficient similarity search.
* Uses **Groq's Llama 3.1-8B-Instant model** for answering questions.
* Defines a **RetrievalQA chain** that retrieves the most relevant sections of the constitution and generates a clear, numbered answer.
* Exposes a web route (`/`) that allows users to enter questions and get answers.

Key libraries used:

* `Flask` (for the web app)
* `LangChain` (for document processing and retrieval)
* `FAISS` (for vector storage)
* `HuggingFace Embeddings` (for semantic similarity)
* `Groq LLM` (for generating answers)

### 2. `chat.html`

This file provides the **frontend web interface** of the chatbot. It contains:

* An input form where users can type questions.
* A section to display the AI-generated answers in a readable format.
* Basic HTML structure styled for usability.

Together, `app.py` (backend) and `chat.html` (frontend) create a working chatbot web application.

---

## 🚀 How It Works

1. The user opens the chatbot webpage.
2. They type a question about the **Constitution of Kenya (2010)**.
3. The system retrieves the most relevant text sections using **FAISS**.
4. The **Groq LLM** processes the retrieved context and generates an answer.
5. The answer is displayed in numbered paragraphs for clarity.

---

## ⚙️ Setup Instructions

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/kenya-constitution-chatbot.git
   cd kenya-constitution-chatbot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add your **Groq API key** to a `.env` file:

   ```env
   GROQ_API_KEY=your_api_key_here
   ```

4. Ensure the file `The_Constitution_of_Kenya_2010.pdf` is in the project root.

5. Run the app:

   ```bash
   python app.py
   ```

6. Open your browser at:

   ```
   http://127.0.0.1:5000
   ```

---

## 📖 Use Case

This project demonstrates how AI can be applied to **legal and educational contexts**, making it easier for citizens, students, and researchers to quickly access information from the Constitution of Kenya.

It can also serve as part of your **portfolio** to showcase skills in:

* Flask Web Development
* Natural Language Processing (NLP)
* LangChain and RAG (Retrieval Augmented Generation)
* Working with Large Language Models (LLMs)

---

