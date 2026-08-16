"""
Search Repository utilizing ChromaDB for Vector Similarity and Embeddings.
"""
from typing import List, Dict, Any
from app.database import get_chroma_collection
from app.utils import generate_simple_embedding

class SearchRepository:
    def __init__(self):
        self.collection = get_chroma_collection()

    def index_product(self, product_id: str, title: str, description: str, brand: str, category: str):
        """Add or update product document vector embedding in ChromaDB."""
        text_content = f"{title} {description or ''} {brand or ''} {category or ''}"
        embedding = generate_simple_embedding(text_content)
        
        self.collection.upsert(
            ids=[product_id],
            embeddings=[embedding],
            metadatas=[{
                "title": title,
                "brand": brand or "",
                "category": category or ""
            }],
            documents=[text_content]
        )

    def search_semantic(self, query: str, limit: int = 10) -> List[str]:
        """Perform vector similarity search against ChromaDB product store."""
        if not query:
            return []
        query_embedding = generate_simple_embedding(query)
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=limit
        )
        if results and "ids" in results and results["ids"]:
            return results["ids"][0]
        return []

    def get_similar_products(self, product_id: str, limit: int = 5) -> List[str]:
        """Find related/similar products using vector distance in ChromaDB."""
        existing = self.collection.get(ids=[product_id], include=["embeddings"])
        if existing and existing.get("embeddings") and len(existing["embeddings"]) > 0:
            embedding = existing["embeddings"][0]
            results = self.collection.query(
                query_embeddings=[embedding],
                n_results=limit + 1
            )
            if results and "ids" in results and results["ids"]:
                ids = results["ids"][0]
                return [i for i in ids if i != product_id][:limit]
        return []
