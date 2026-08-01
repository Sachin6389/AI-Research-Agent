from langgraph.graph import StateGraph, END
from src.State import ReSearchAgentState
from langchain_groq import ChatGroq
from src.Tools import search_web, read_webpage
from src.Prompt import SUMMARY_PROMPT, REPORT_PROMPT
from dotenv import load_dotenv
import os

load_dotenv()


# =========================================================
# LLM
# =========================================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)


# =========================================================
# 1. SEARCH NODE
# =========================================================

def search_node(state: ReSearchAgentState):

    query = state["query"]

    

    results = search_web(query)

    

    return {
        "search_results": results
    }


# =========================================================
# 2. SCRAPE NODE
# =========================================================

def scrape_node(state: ReSearchAgentState):

    pages = []

    search_results = state.get("search_results", [])

    for result in search_results:

        if isinstance(result, dict):

            url = result.get("url", "")
            title = result.get("title", "")

        else:

            url = result
            title = ""

        if not url:
            continue

        

        try:

            page_text = read_webpage(url)

            if page_text:

                pages.append({
                    "title": title,
                    "url": url,
                    "content": page_text
                })

        except Exception as e:

            print(f"❌ Error reading {url}: {e}")

    

    return {
        "web_pages": pages
    }


# =========================================================
# 3. SUMMARIZE NODE
# =========================================================

def summarize_node(state: ReSearchAgentState):

    query = state["query"]

    notes = []

    web_pages = state.get("web_pages", [])

    for article in web_pages:

        title = article.get("title", "")
        url = article.get("url", "")
        content = article.get("content", "")

        

        prompt = SUMMARY_PROMPT.format(
            query=query,
            title=title,
            url=url,
            content=content
        )

        try:

            response = llm.invoke(prompt)

            summary = response.content

            

            notes.append({
                "title": title,
                "url": url,
                "notes": summary
            })

        except Exception as e:

            print(f"❌ Error summarizing {title}: {e}")

    return {
        "notes": notes
    }


# =========================================================
# 4. REPORT NODE
# =========================================================

def report_node(state: ReSearchAgentState):

    query = state["query"]

    research_data = ""

    notes = state.get("notes", [])

    for item in notes:

        research_data += f"""
----------------------------------------

SOURCE TITLE:
{item.get("title", "")}

SOURCE URL:
{item.get("url", "")}

RESEARCH NOTES:
{item.get("notes", "")}

----------------------------------------
"""

    prompt = REPORT_PROMPT.format(
        query=query,
        research_data=research_data
    )

    response = llm.invoke(prompt)

    return {
        "report": response.content
    }


# =========================================================
# LANGGRAPH
# =========================================================

builder = StateGraph(ReSearchAgentState)


# =========================================================
# NODES
# =========================================================

builder.add_node(
    "search",
    search_node
)

builder.add_node(
    "scrape",
    scrape_node
)

builder.add_node(
    "summarize",
    summarize_node
)

builder.add_node(
    "report",
    report_node
)


# =========================================================
# WORKFLOW
# =========================================================

builder.set_entry_point("search")

builder.add_edge(
    "search",
    "scrape"
)

builder.add_edge(
    "scrape",
    "summarize"
)

builder.add_edge(
    "summarize",
    "report"
)

builder.add_edge(
    "report",
    END
)


# =========================================================
# COMPILE
# =========================================================

graph = builder.compile()