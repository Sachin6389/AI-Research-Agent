import os
import requests

from bs4 import BeautifulSoup
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_web(query):

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )
    results = []

    for result in response["results"]:

        results.append({
            "title": result.get("title", ""),
            "url": result.get("url", ""),
            "content": result.get("content", "")
        })

    return results


def read_webpage(url):

    try:

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )
        

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )
        

        # Remove unnecessary HTML
        for tag in soup([
            "script",
            "style",
            "nav",
            "footer",
            "header"
        ]):
            tag.decompose()

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        return text[:10000]

    except Exception as e:

        print(f"Error reading {url}: {e}")

        return ""