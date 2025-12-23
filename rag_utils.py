import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# ----------------------------
# Load Documents
# ----------------------------
with open("data/documents.json", "r") as f:
    documents = json.load(f)

# ----------------------------
# Chunk Documents
# ----------------------------
chunks = []
for doc in documents:
    for section, text in doc["sections"].items():
        for para in text.split("."):
            para = para.strip()
            if para:
                chunks.append({
                    "text": para,
                    "doc": doc["title"],
                    "section": section
                })

# ----------------------------
# Embeddings
# ----------------------------
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embed_model.encode([c["text"] for c in chunks], normalize_embeddings=True)

# ----------------------------
# FAISS Index
# ----------------------------
dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)
index.add(np.array(embeddings))

# ----------------------------
# Retrieve Top-K
# ----------------------------
def retrieve(query, k=3):
    q_emb = embed_model.encode([query], normalize_embeddings=True)
    scores, ids = index.search(np.array(q_emb), k)
    results = []
    for score, idx in zip(scores[0], ids[0]):
        results.append({
            "score": round(float(score), 2),
            **chunks[idx]
        })
    return results

# ----------------------------
# Grounded Answer Generator
# ----------------------------
def generate_answer(query, retrieved):
    if not retrieved:
        return "I don't have enough information from the provided documents."

    # Strict grounding: answer built only from retrieved chunks
    answer = " ".join(r["text"] for r in retrieved)
    return answer
