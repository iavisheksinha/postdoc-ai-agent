# Postdoc AI Agent

An AI-powered research assistant for discovering postdoctoral opportunities using intelligent academic web search, local LLMs, and LangGraph workflows.

## Features

* Local LLM inference using Ollama (Llama 3)
* Interactive Streamlit web interface
* Country-aware academic opportunity search
* AI-powered opportunity analysis and summarization
* Ranked postdoctoral opportunity recommendations
* Academic web search using DDGS
* LangGraph workflow orchestration
* Fully local AI processing (except web search)

## Technology Stack

* Python
* Streamlit
* Ollama
* Llama 3
* DDGS
* LangChain
* LangGraph
* Git

## Current Status

### Version 0.4

Implemented:

* Academic opportunity discovery
* Country-specific search filters

  * Japan
  * USA
  * Germany
  * UK
* LangGraph workflow integration
* AI-generated summaries
* Opportunity ranking and recommendations
* GitHub version control
* Streamlit-based user interface

## Current Workflow

User Query
→ Country Selection
→ Smart Academic Search (DDGS)
→ LangGraph Search Node
→ LangGraph Summary Node
→ AI Analysis (Llama 3)
→ Ranked Opportunities
→ Streamlit Display

## Project Structure

```text
postdoc_ai_agent/
│
├── app.py                # Streamlit frontend
├── graph.py              # LangGraph workflow
├── test_search.py        # Search experiments
├── README.md
└── .gitignore
```

## Planned Features

### Version 0.5

* Excel export of opportunities
* Clickable opportunity links
* Better university and institute filtering
* Opportunity scoring system

### Version 0.6

* Professor matching
* Research-interest matching
* Automated opportunity tracking

### Version 1.0

* Multi-agent LangGraph architecture
* Email generation for professors
* CV analysis and feedback
* Personalized recommendation engine
* Postdoc application assistant

## Motivation

Finding suitable postdoctoral opportunities often requires searching across multiple university, government, and research institute websites. This project aims to automate discovery, filtering, ranking, and analysis of opportunities using modern AI tools and agentic workflows.

## Author

Avishek Sinha

PhD, Computer Science & Engineering
