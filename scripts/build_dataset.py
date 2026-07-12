import json
from pathlib import Path
import arxiv


def paper_to_document(index, paper):

    return {
        "id": index,
        "title": paper.title.strip(),
        "author": ", ".join(
            author.name
            for author in paper.authors
        ),
        "category": paper.primary_category,
        "pages": 0,
        "language": "English",
        "tags": paper.categories,
        "content": paper.summary.replace("\n", " "),
        "year": paper.published.year,
        "source": paper.entry_id,
        "pdf_url": paper.pdf_url,
    }


queries = [

    "transformer",

    "large language model",

    "retrieval augmented generation",

    "computer vision",

    "reinforcement learning",

    "diffusion model",

    "multimodal AI"
]

documents = []

index = 1
client = arxiv.Client()

for query in queries:

    search = arxiv.Search(
        query=query,
        max_results=3,
        sort_by=arxiv.SortCriterion.Relevance
    )

    for paper in client.results(search):

        documents.append(
            paper_to_document(index, paper)
        )
        index += 1

unique = {}

for doc in documents:
    unique[doc["title"]] = doc
documents = list(unique.values())

for i, doc in enumerate(documents, start=1):
    doc["id"] = i

output = (
    Path(__file__).parent.parent
    / "data"
    / "documents.json"
)
with open(output, "w", encoding="utf_8") as file:
    json.dump(
        documents,
        file,
        indent=4,
        ensure_ascii=False
    )
print(f"{len(documents)} papers saved.")
