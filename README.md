# Construction Marketplace RAG Assistant

This project implements a **Retrieval-Augmented Generation (RAG)** system for a
construction marketplace AI assistant. The assistant answers user questions
**strictly using internal documents** such as policies, FAQs, and specifications,
ensuring transparency and avoiding hallucinations or unsupported claims.

The project demonstrates document chunking, semantic retrieval, and grounded
answer generation with clear explainability.

---

## Project Architecture

The system follows a standard RAG pipeline:

Documents → Chunking → Embeddings → FAISS Vector Index → Top-K Retrieval → Grounded Answer

For every user query:
1. Relevant document chunks are retrieved using semantic similarity.
2. The answer is generated **only from the retrieved chunks**.
3. The retrieved context and the final answer are clearly displayed.

---

## Embedding Model

- **Model Used:** `sentence-transformers/all-MiniLM-L6-v2`
- **Reason for Selection:**
  - Lightweight and fast
  - Open-source and widely adopted
  - Produces high-quality embeddings for semantic search
  - Works efficiently with FAISS

Each document chunk is converted into a dense vector embedding using this model.

---

## Language Model (LLM)

- **Approach Used:** Grounded / deterministic answer generation
- **Reason:**
  - The execution environment (Kaggle) restricts downloading large Hugging Face models.
  - To ensure reproducibility and correctness, answers are generated strictly from
    retrieved document content.

The RAG pipeline is **model-agnostic** and can be extended to use:
- Local open-source LLMs (TinyLlama, Phi-2 via Hugging Face or Ollama)
- API-based LLMs (OpenRouter)

---

## Document Processing (Chunking)

Internal documents are stored in `data/documents.json`.

### Chunking Strategy
- Documents are split into **logical sections** (policies, FAQs, specifications).
- Sections are further divided into **meaningful paragraph-level chunks**.
- Each chunk retains metadata:
  - Document title
  - Section name

This improves retrieval relevance and answer traceability.

---

## Vector Indexing and Retrieval

- **Vector Store:** FAISS (CPU-based)
- **Similarity Metric:** Cosine similarity
- **Retrieval Strategy:** Top-K semantic retrieval (K = 3)

### Retrieval Process
1. User query is embedded using the same embedding model.
2. FAISS retrieves the top-K most relevant document chunks.
3. Retrieved chunks are passed to the answer generator as context.

---

## Grounded Answer Generation

The system enforces **strict grounding rules**:

- Answers are generated **only from retrieved document chunks**.
- No external knowledge is used.
- If the retrieved documents do not explicitly contain the answer, the system responds with:



This behavior is intentional and prevents hallucinations.

---

## Transparency and Explainability

For every query, the system clearly displays:

1. **Retrieved Context**
   - Top-K document chunks
   - Source document and section
   - Similarity scores

2. **Final Answer**
   - Fully grounded in retrieved content
   - Or a safe refusal when information is missing

---

## Evaluation and Quality Analysis

The system was tested using multiple questions derived from the internal documents.

### Evaluation Focus
- Relevance of retrieved document chunks
- Correct refusal behavior when information is absent
- Absence of hallucinations
- Clarity and completeness of generated answers

### Observations
- Retrieval consistently returned policy-relevant chunks.
- The system correctly refused to answer when documents lacked explicit information.
- No unsupported or hallucinated claims were observed.

---

## Optional Enhancements (Bonus)

### Local Open-Source LLM Usage

An attempt was made to run a local open-source LLM (TinyLlama via Hugging Face Transformers).
However, due to network restrictions in the Kaggle environment, downloading the model
was not possible.

The RAG pipeline remains unchanged and can be easily extended to use:
- Local LLMs via Hugging Face or Ollama
- OpenRouter-based LLMs

---

### Conceptual Comparison: Local LLM vs OpenRouter

| Aspect        | Local Open-Source LLM | OpenRouter LLM |
|--------------|----------------------|----------------|
| Latency      | Low (local inference) | Medium (API-based) |
| Cost         | Free after setup      | Pay-per-use |
| Privacy      | Fully local           | External service |
| Groundedness | High (prompt-controlled) | High (prompt-controlled) |

---

## Running the Project Locally

### Requirements
Install dependencies using:

```bash
pip install -r requirements.txt
