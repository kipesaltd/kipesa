import numpy as np
from typing import List, Dict, Any, Optional
from loguru import logger

# Try to import ML dependencies with fallback
try:
    from sentence_transformers import SentenceTransformer
    from sklearn.metrics.pairwise import cosine_similarity
    ML_AVAILABLE = True
    logger.info("ML dependencies available for semantic search")
except ImportError as e:
    logger.warning(f"ML dependencies not available: {e}. Semantic search will be disabled.")
    ML_AVAILABLE = False

class SemanticSearchService:
    """Semantic search service for knowledge base content."""
    
    def __init__(self):
        if not ML_AVAILABLE:
            self.model = None
            self.embeddings_cache = {}
            self.similarity_threshold = 0.3
            logger.warning("Semantic search disabled - ML dependencies not available")
            return
            
        # Initialize sentence transformer model
        try:
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            self.embeddings_cache = {}
            self.similarity_threshold = 0.3
            logger.info("Semantic search service initialized")
        except Exception as e:
            logger.error(f"Failed to initialize semantic search: {e}")
            self.model = None
    
    def get_embedding(self, text: str) -> Optional[np.ndarray]:
        """Get embedding for text."""
        if not self.model:
            return None
            
        if text in self.embeddings_cache:
            return self.embeddings_cache[text]
        
        try:
            embedding = self.model.encode(text)
            self.embeddings_cache[text] = embedding
            return embedding
        except Exception as e:
            logger.error(f"Error getting embedding: {e}")
            return None
    
    def find_similar_content(
        self, 
        query: str, 
        knowledge_items: List[Dict[str, Any]], 
        top_k: int = 3
    ) -> List[Dict[str, Any]]:
        """Find similar content using semantic search."""
        if not self.model:
            logger.debug("Semantic search not available, returning empty results")
            return []
            
        try:
            if not knowledge_items:
                return []
            
            # Get query embedding
            query_embedding = self.get_embedding(query)
            if query_embedding is None:
                return []
            
            # Get embeddings for all knowledge items
            item_embeddings = []
            for item in knowledge_items:
                # Combine title and content for embedding
                text = f"{item['title']} {item['content']}"
                embedding = self.get_embedding(text)
                if embedding is not None:
                    item_embeddings.append(embedding)
                else:
                    # Skip items that can't be embedded
                    continue
            
            if not item_embeddings:
                return []
            
            # Calculate similarities
            similarities = cosine_similarity([query_embedding], item_embeddings)[0]
            
            # Create results with similarity scores
            results = []
            for i, item in enumerate(knowledge_items):
                if i < len(similarities):
                    similarity = similarities[i]
                    if similarity >= self.similarity_threshold:
                        results.append({
                            **item,
                            'similarity_score': float(similarity)
                        })
            
            # Sort by similarity score and return top_k
            results.sort(key=lambda x: x['similarity_score'], reverse=True)
            return results[:top_k]
            
        except Exception as e:
            logger.error(f"Error in semantic search: {e}")
            return []
    
    def update_embeddings_cache(self, knowledge_items: List[Dict[str, Any]]):
        """Update embeddings cache with new knowledge items."""
        if not self.model:
            return
            
        for item in knowledge_items:
            text = f"{item['title']} {item['content']}"
            if text not in self.embeddings_cache:
                self.get_embedding(text)

# Global semantic search service
semantic_search_service = SemanticSearchService() 