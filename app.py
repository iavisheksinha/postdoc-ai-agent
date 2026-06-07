import streamlit as st
from ddgs import DDGS
from langchain_ollama import ChatOllama

st.title("Postdoc AI Agent")

country = st.selectbox(
    "Select Country",
    ["Japan", "USA", "Germany", "UK"]
)

query = st.text_input("Enter your query:")

if query:

    if country == "Japan":
        sites = "site:riken.jp OR site:nii.ac.jp OR site:jst.go.jp"

    elif country == "USA":
        sites = "site:edu OR site:microsoft.com OR site:openai.com"

    elif country == "Germany":
        sites = "site:mpg.de OR site:tum.de"

    elif country == "UK":
        sites = "site:ox.ac.uk OR site:cam.ac.uk"

    smart_query = f"""
    postdoctoral researcher {query}
    {sites}
    """

    results = list(
        DDGS().text(
            smart_query,
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
You are an academic career advisor.

Analyze the following postdoctoral search results.

{search_text}

Provide:

1. A short summary.
2. Top opportunities ranked from best to worst.
3. Why each opportunity is relevant.
4. Recommendations for the applicant.
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