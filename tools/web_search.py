from duckduckgo_search import DDGS

def search_web(query, max_results=5):
    results_text = ""

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)

        for r in results:
            results_text += f"""
Title: {r['title']}
Snippet: {r['body']}
URL: {r['href']}
---
"""

    return results_text