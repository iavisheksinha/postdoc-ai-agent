# Postdoc AI Agent

An AI-powered research assistant for discovering postdoctoral opportunities using intelligent academic web search, local LLMs, and LangGraph-based workflows.

## Features

* Local LLM inference using Ollama (Llama 3)
* Interactive Streamlit web interface
* Country-aware academic opportunity search
* AI-powered opportunity analysis and summarization
* Academic web search using DDGS
* LangGraph workflow orchestration
* Structured search result display
* Fully local AI processing (except web search)

## Technology Stack

* Python
* Streamlit
* Ollama
* Llama 3
* DDGS
* LangChain
* LangGraph
* Git & GitHub

## Current Status

### Version 0.5

Implemented:

* Academic opportunity discovery
* Country-specific search filters

  * Japan
  * USA
  * Germany
  * UK
* LangGraph integration
* Search Node
* Decision Node
* Summary Node
* AI-generated summaries
* Structured search result display
* GitHub version control
* Streamlit-based user interface

## Current Workflow

User Query
→ Country Selection
→ Smart Academic Search (DDGS)
→ LangGraph Search Node
→ LangGraph Decision Node
→ LangGraph Summary Node
→ AI Analysis (Llama 3)
→ Streamlit Display

## Project Structure

```text
postdoc_ai_agent/
│
├── app.py                # Streamlit frontend
├── graph.py              # LangGraph workflow
├── langgraph_test.py     # LangGraph experiments
├── test_search.py        # Search experiments
├── README.md
└── .gitignore
```

## Current Architecture

```text
User Query
     ↓
Search Node
     ↓
Decision Node
     ↓
Summary Node
     ↓
Display Results
```

## Planned Features

### Version 0.6

* Dynamic routing in LangGraph
* Search refinement node
* Opportunity scoring and ranking
* Excel export

### Version 0.7

* Professor matching
* Research-interest matching
* Automated opportunity tracking
* Saved searches

### Version 1.0

* Multi-agent LangGraph architecture
* Email generation for professors
* CV analysis and feedback
* Personalized recommendation engine
* Postdoc application assistant

## Motivation

Finding suitable postdoctoral opportunities often requires searching across multiple university, government, and research institute websites. This project aims to automate discovery, filtering, ranking, and analysis of opportunities using modern AI techniques and agentic workflows.

## Learning Goals

This project is being developed as a practical exploration of:

* Local LLM deployment with Ollama
* Agentic AI systems
* LangGraph workflows
* Research opportunity discovery
* AI-assisted academic career support

## Author

Avishek Sinha

PhD, Computer Science & Engineering
