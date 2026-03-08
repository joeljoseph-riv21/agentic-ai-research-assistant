from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(query):
    response = tavily.search(query=query, max_results=5)
    results = []

    for r in response["results"]:
        results.append({
            "title": r["title"],
            "url": r["url"],
            "content": r["content"]
        })

    return results