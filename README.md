# Build-a-Mini-RAG
 # Construction Marketplace RAG Assistant

This project implements a Retrieval-Augmented Generation (RAG) system for a
construction marketplace AI assistant. The assistant answers user questions
strictly using internal documents such as policies, FAQs, and specifications.

---

## Embedding Model

- Model: sentence-transformers (all-MiniLM-L6-v2)
- Reason: Lightweight, open-source, fast, and effective for semantic search.

---

## Document Chunking

Documents are split into meaningful sections and paragraphs.
Each chunk retains:
- Document name
- Section name

This improves retrieval accuracy and transparency.

---

## Vector Search

- FAISS is used as a local vector database.
- Each document chunk is embedded and indexed.
- For every user query, the top-K most relevant chunks are retrieved using
  semantic similarity.

---

## Grounded Answer Generation

The system generates answers strictly from retrieved document chunks.
If the documents do not contain enough information, the system responds with:

"I don't have enough information from the provided documents."

This behavior prevents hallucinations and unsupported claims.

---

## Transparency

Each response clearly displays:
1. Retrieved document chunks (context)
2. Final generated answer

---

## Limitations

Due to network restrictions in the execution environment, downloading and running
a local Hugging Face LLM was not possible. Therefore, a deterministic grounded
answer generator was used. The RAG pipeline itself remains unchanged and
model-agnostic.

---

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the notebook or script to see retrieved context and final answers.
## Running the Project (Kaggle)

This project was developed and tested in Kaggle notebooks.
Due to restricted internet access in Kaggle, downloading large
Hugging Face models is not always possible.

The system therefore demonstrates:
- Document chunking
- Embedding generation
- FAISS-based retrieval
- Strict grounding and refusal behavior

All outputs shown in the notebook are reproducible in Kaggle.

