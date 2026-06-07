import streamlit as st
from ddgs import DDGS

st.title("Postdoc AI Agent")

query = st.text_input("Enter your query:")

if query:

    results = list(
        DDGS().text(
            query,
            max_results=5
        )
    )

    st.subheader("Search Results")

    for i, result in enumerate(results, start=1):
        st.write(f"### {i}. {result['title']}")
        st.write(result["href"])
        st.write(result["body"])
        st.write("---")