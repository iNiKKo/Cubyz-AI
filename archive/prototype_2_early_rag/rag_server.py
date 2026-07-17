import os
import json
import urllib.request
import chromadb
from chromadb.utils import embedding_functions
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Cubyz Distributed RAG Core")

# --- CONFIGURATION ---
USERS_DIR = "users"
DB_DIR = "./cubyz_vectordb"
OLLAMA_URL = "http://localhost:11434/api/generate"
LLM_MODEL = "qwen3:14b"  # Replace with whichever model you run locally

# Initialize persistent ChromaDB local database
print("[~] Initializing ChromaDB vector engine...")
db_client = chromadb.PersistentClient(path=DB_DIR)
# Chroma's default sentence-transformer converts text into vectors locally
emb_fn = embedding_functions.DefaultEmbeddingFunction()
collection = db_client.get_or_create_collection("cubyz_knowledge", embedding_function=emb_fn)


def build_or_update_database():
    """Dynamically reads all user datasets and populates the Chroma database."""
    if not os.path.exists(USERS_DIR):
        print(f"[X] Directory '{USERS_DIR}' not found. Cannot load context data.")
        return

    print("[~] Scanning user directories to merge volunteer datasets...")
    documents = []
    metadatas = []
    ids = []

    chunk_counter = 0

    # Read dataset.jsonl from every volunteer directory
    for user_folder in os.listdir(USERS_DIR):
        user_path = os.path.join(USERS_DIR, user_folder)
        if not os.path.isdir(user_path):
            continue

        dataset_path = os.path.join(user_path, "dataset.jsonl")
        if not os.path.exists(dataset_path):
            continue

        print(f"  ↳ Consolidating records for worker: {user_folder}")
        try:
            with open(dataset_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        chunk = json.loads(line)

                        # Prepare the searchable text (What the database searches against)
                        searchable_text = f"Summary: {chunk['summary']}\nQueries: " + " | ".join(chunk['synthetic_queries'])

                        # Store the highly technical payload as metadata for retrieval
                        metadata = {
                            "chunk_id": chunk["chunk_id"],
                            "title": chunk["title"],
                            "user_id": chunk["user_id"],
                            "explanation": chunk["comprehensive_explanation"],
                            "code_example": chunk["code_example"] or "No code example provided."
                        }

                        documents.append(searchable_text)
                        metadatas.append(metadata)
                        ids.append(f"doc_{chunk_counter}")
                        chunk_counter += 1
                    except Exception as e:
                        print(f"    [!] Skipping corrupt/incomplete line in {user_folder}'s dataset: {e}")
        except Exception as e:
            print(f"    [X] Failed reading database file for {user_folder}: {e}")

    if not documents:
        print("[!] No volunteer data found on disk yet.")
        return

    print(f"[~] Writing {len(documents)} total consolidated vector chunks into ChromaDB...")

    # We use upsert so restarting the server updates existing chunks cleanly without duplicates
    collection.upsert(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    print("[✓] Vector database is synchronized and ready for RAG query routing!")


# Execute data compilation and indexing at startup
build_or_update_database()


class ChatQuery(BaseModel):
    question: str


def query_ollama(prompt: str) -> str:
    """Helper to query the local Ollama daemon."""
    payload = {
        "model": LLM_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.0}  # Low temperature guarantees factual fidelity
    }
    try:
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(OLLAMA_URL, data=data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req, timeout=120) as res:
            response = json.loads(res.read().decode('utf-8'))
            return response.get("response", "")
    except Exception as e:
        return f"Error communicating with local Ollama engine: {e}"


@app.post("/ask")
def ask_rag(query: ChatQuery):
    """
    Search vector database for the top 3 closest matches,
    inject them into the context window, and generate an answer.
    """
    # 1. Search vector DB for nearest neighbor context match
    results = collection.query(
        query_texts=[query.question],
        n_results=3
    )

    if not results or not results['metadatas'] or not results['metadatas'][0]:
        raise HTTPException(status_code=404, detail="No matching code context found in the database.")

    # 2. Extract and format the context for the model's prompt
    retrieved_context = ""
    for idx, meta in enumerate(results['metadatas'][0]):
        retrieved_context += f"--- CONTEXT REFERENCE {idx+1} ({meta['title']}) ---\n"
        retrieved_context += f"Explanation: {meta['explanation']}\n"
        retrieved_context += f"Code Example:\n{meta['code_example']}\n\n"

    # 3. Compile the rigid RAG system prompt
    rag_prompt = f"""You are a specialized developer AI assistant for the Cubyz voxel engine.
Your goal is to answer technical questions strictly utilizing the retrieved codebase context below.

Rules:
- Be technically precise, factual, and direct.
- Do NOT make up information or introduce external features.
- If the retrieved context is missing information to answer completely, state that you do not have enough specific data.

Retrieved Codebase Context:
{retrieved_context}

User Question: {query.question}

Technical Answer:"""

    # 4. Generate & stream the accurate answer
    ai_response = query_ollama(rag_prompt)

    return {
        "answer": ai_response,
        "sources": [meta['title'] for meta in results['metadatas'][0]]
    }


if __name__ == "__main__":
    import uvicorn
    # Launches on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
