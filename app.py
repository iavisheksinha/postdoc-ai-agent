import streamlit as st
from graph import app

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

    response = app.invoke(
        {
            "query": smart_query
        }
    )

    st.subheader("AI Summary")
    st.write(response["summary"])

    st.subheader("Search Results")

    for i, result in enumerate(response["results"], start=1):
        st.write(f"### {i}. {result['title']}")
        st.write(result["href"])
        st.write(result["body"])
        st.write("---")