"""
ingest.py — Run once to chunk, embed, and load the knowledge base into Pinecone.
Usage: python demo/ingest.py
"""
import os, sys, time
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec

openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

INDEX_NAME = "kearney-demo"
DIMENSION = 1536  # text-embedding-3-small


def ensure_index():
    existing = [i.name for i in pc.list_indexes()]
    if INDEX_NAME not in existing:
        print(f"Creating Pinecone index '{INDEX_NAME}'...")
        pc.create_index(
            name=INDEX_NAME,
            dimension=DIMENSION,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        print("Waiting for index to be ready...")
        time.sleep(15)
    else:
        print(f"Index '{INDEX_NAME}' already exists.")
    return pc.Index(INDEX_NAME)


def chunk_text(text: str, chunk_size: int = 350, overlap: int = 70) -> list[str]:
    """Split text into overlapping word-based chunks."""
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))
        if end == len(words):
            break
        start += chunk_size - overlap
    return chunks


def embed(text: str) -> list[float]:
    response = openai_client.embeddings.create(
        input=text, model="text-embedding-3-small"
    )
    return response.data[0].embedding


def ingest_file(index, file_path: Path, source_name: str):
    text = file_path.read_text(encoding="utf-8")
    chunks = chunk_text(text)
    print(f"  {source_name}: {len(chunks)} chunks")

    vectors = []
    for i, chunk in enumerate(chunks):
        vec = embed(chunk)
        vectors.append({
            "id": f"{source_name}-chunk-{i}",
            "values": vec,
            "metadata": {
                "text": chunk,
                "source": source_name,
                "chunk_index": i,
            },
        })
        print(f"    Embedded {i + 1}/{len(chunks)}", end="\r", flush=True)

    # Upsert in batches of 50
    for i in range(0, len(vectors), 50):
        index.upsert(vectors=vectors[i : i + 50])
    print(f"    Uploaded {len(vectors)} chunks.")


if __name__ == "__main__":
    index = ensure_index()

    base = Path(__file__).parent.parent
    sources = [
        (base / "research" / "2026-03-06-agentic-ai-trends.md", "agentic-ai-trends"),
    ]

    print("\nIngesting documents...")
    for path, name in sources:
        if path.exists():
            ingest_file(index, path, name)
        else:
            print(f"  WARNING: {path} not found, skipping.")

    stats = index.describe_index_stats()
    print(f"\nDone. Index '{INDEX_NAME}' now has {stats['total_vector_count']} vectors.")
