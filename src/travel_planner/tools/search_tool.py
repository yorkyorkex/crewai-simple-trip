from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests
import os
import hashlib
import time
from functools import lru_cache


class SearchToolInput(BaseModel):
    """Input schema for SearchTool."""
    query: str = Field(..., description="The search query to find information about travel destinations, attractions, restaurants, etc.")


class SearchTool(BaseTool):
    name: str = "Search Tool"
    description: str = (
        "A tool to search for current information about travel destinations, attractions, restaurants, "
        "weather conditions, and other travel-related topics using Serper API."
    )
    args_schema: Type[BaseModel] = SearchToolInput

    # Class-level cache with TTL
    _cache = {}
    _cache_ttl = 3600  # 1 hour

    def _get_cache_key(self, query: str) -> str:
        """Generate cache key from query."""
        return hashlib.md5(query.lower().encode()).hexdigest()

    def _is_cache_valid(self, timestamp: float) -> bool:
        """Check if cache entry is still valid."""
        return (time.time() - timestamp) < self._cache_ttl

    def _run(self, query: str) -> str:
        """Search for information using Serper API with caching."""
        try:
            # Check cache first
            cache_key = self._get_cache_key(query)
            if cache_key in self._cache:
                cached_data, timestamp = self._cache[cache_key]
                if self._is_cache_valid(timestamp):
                    return cached_data

            api_key = os.getenv("SERPER_API_KEY")
            if not api_key:
                return "Error: SERPER_API_KEY not found in environment variables."
            
            url = "https://google.serper.dev/search"
            payload = {
                "q": query,
                "num": 6  # Reduced from 10 for faster responses
            }
            headers = {
                "X-API-KEY": api_key,
                "Content-Type": "application/json"
            }
            
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            
            if response.status_code == 200:
                results = response.json()
                
                # Format the search results
                formatted_results = []
                
                # Add organic results
                if "organic" in results:
                    for result in results["organic"][:5]:  # Reduced for efficiency
                        formatted_results.append(f"**{result.get('title', 'No Title')}**\n{result.get('snippet', 'No description available')}\n")

                # Add knowledge graph info if available
                if "knowledgeGraph" in results:
                    kg = results["knowledgeGraph"]
                    if "description" in kg:
                        formatted_results.insert(0, f"**{kg['description']}**\n")

                result_text = "\n".join(formatted_results) if formatted_results else "No relevant information found."

                # Cache the result
                self._cache[cache_key] = (result_text, time.time())
                return result_text
            
            else:
                return f"Error: Search request failed with status code {response.status_code}"
                
        except Exception as e:
            return f"Error performing search: {str(e)}"