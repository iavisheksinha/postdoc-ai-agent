from typing import TypedDict

from ddgs import DDGS
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, END


class State(TypedDict):
    query: str
    search_result: str
    results: list
    summary: str
    decision: str


def search_node(state):

    print("Searching...")

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


def decision_node(state):

    print("Making Decision...")

    if len(state["results"]) < 3:
        return {
            "decision": "search_again"
        }

    return {
        "decision": "summarize"
    }


def summary_node(state):

    print("Summarizing...")

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


def route_decision(state):

    return state["decision"]


graph = StateGraph(State)

graph.add_node("search", search_node)
graph.add_node("decision", decision_node)
graph.add_node("summary", summary_node)

graph.set_entry_point("search")

graph.add_edge("search", "decision")

graph.add_conditional_edges(
    "decision",
    route_decision,
    {
        "summarize": "summary",
        "search_again": "summary"
    }
)

graph.add_edge("summary", END)

app = graph.compile()