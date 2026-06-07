from typing import TypedDict

from ddgs import DDGS
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, END


class State(TypedDict):
    query: str
    search_result: str
    results: list
    summary: str


def search_node(state):

    results = list(
        DDGS().text(
            state["query"],
            max_results=5
        )
    )

    search_text = ""

    for result in results:
        search_text += f"""
Title: {result['title']}
URL: {result['href']}
Description: {result['body']}

"""

    return {
        "search_result": search_text,
        "results": results
    }


def summary_node(state):

    llm = ChatOllama(model="llama3")

    prompt = f"""
You are a research assistant.

Based on these search results:

{state["search_result"]}

Provide:
1. A concise summary.
2. Top opportunities.
3. Recommendations.
"""

    response = llm.invoke(prompt)

    return {
        "summary": response.content
    }


graph = StateGraph(State)

graph.add_node("search", search_node)
graph.add_node("summary", summary_node)

graph.set_entry_point("search")

graph.add_edge("search", "summary")
graph.add_edge("summary", END)

app = graph.compile()