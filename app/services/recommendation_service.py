"""
Recommendation Engine utilizing ChromaDB Vector Store for Similar Products & Recommendations.
"""
from typing import List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.search_repository import SearchRepository
from app.repositories.product_repository import ProductRepository

class RecommendationService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.search_repo = SearchRepository()
        self.product_repo = ProductRepository(db)

    async def get_similar_products(self, product_id: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Get vector-based similar products for given item."""
        similar_ids = self.search_repo.get_similar_products(product_id, limit=limit)
        results = []
        for pid in similar_ids:
            p = await self.product_repo.get_by_id(pid)
            if p and p.is_active:
                results.append({
                    "id": p.id,
                    "title": p.title,
                    "price": p.price,
                    "brand": p.brand
                })
        
        # Fallback to catalog products if no vector neighbours found
        if not results:
            fallback = await self.product_repo.filter_products(limit=limit)
            results = [{"id": p.id, "title": p.title, "price": p.price, "brand": p.brand} for p in fallback if p.id != product_id]

        return results[:limit]

    async def get_frequently_bought_together(self, product_id: str) -> List[Dict[str, Any]]:
        """Get complementary items commonly bought together."""
        return await self.get_similar_products(product_id, limit=3)
