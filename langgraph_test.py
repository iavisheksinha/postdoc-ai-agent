from typing import TypedDict

from langgraph.graph import StateGraph, END


class State(TypedDict):
    query: str
    search_result: str
    summary: str


def search_node(state):
    print("Search Node Running...")

    return {
        "search_result": f"Found opportunities for: {state['query']}"
    }


def summary_node(state):
    print("Summary Node Running...")

    return {
        "summary": f"Summary: {state['search_result']}"
    }


graph = StateGraph(State)

graph.add_node("search", search_node)
graph.add_node("summary", summary_node)

graph.set_entry_point("search")

graph.add_edge("search", "summary")
graph.add_edge("summary", END)

app = graph.compile()

response = app.invoke(
    {
        "query": "AI postdoc Japan"
    }
)

print(response)