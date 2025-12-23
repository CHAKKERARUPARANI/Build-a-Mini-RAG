import streamlit as st
from rag_utils import retrieve, generate_answer

st.set_page_config(page_title="Construction RAG Assistant", layout="wide")

st.title("🏗️ Construction Marketplace RAG Assistant")

st.markdown("""
Ask questions related to construction policies, guarantees, FAQs, and specifications.
The assistant answers **only using internal documents**.
""")

query = st.text_input("Enter your question:")

if query:
    with st.spinner("Retrieving relevant documents..."):
        retrieved = retrieve(query)

    st.subheader("📄 Retrieved Context (Top-K)")
    for r in retrieved:
        st.markdown(f"""
**Score:** {r['score']}  
**Source:** {r['doc']} → {r['section']}  
{r['text']}
---
""")

    st.subheader("✅ Final Answer")
    answer = generate_answer(query, retrieved)
    st.success(answer)
