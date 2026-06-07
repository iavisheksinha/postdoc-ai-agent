import streamlit as st
from ddgs import DDGS
from langchain_ollama import ChatOllama

st.title("Postdoc AI Agent")

query = st.text_input("Enter your query:")

if query:

    results = list(
        DDGS().text(
            query,
            max_results=5
        )
    )

    llm = ChatOllama(model="llama3")

    search_text = ""

    for result in results:
        search_text += f"""
Title: {result['title']}
URL: {result['href']}
Description: {result['body']}

"""

    prompt = f"""
You are a research assistant helping users find postdoctoral opportunities.

Based on the following search results:

{search_text}

Provide:
1. A concise summary.
2. The most promising opportunities.
3. Any recommendations for the user.
"""

    response = llm.invoke(prompt)

    st.subheader("AI Summary")
    st.write(response.content)

    st.subheader("Search Results")

    for i, result in enumerate(results, start=1):
        st.write(f"### {i}. {result['title']}")
        st.write(result["href"])
        st.write(result["body"])
        st.write("---")