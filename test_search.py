from ddgs import DDGS

results = list(
    DDGS().text(
        "postdoctoral researcher artificial intelligence japan",
        max_results=5
    )
)

print(results)