from models.document import Document
from managers.knowledge_base_manager import KnowledgeBaseManager
from loaders.json_loader import JsonLoader


loader = JsonLoader("src/python/ai-research-library/data/documents.json")
documents = loader.load()
manager = KnowledgeBaseManager()

for document in documents:
    manager.add_document(document)

print("=" * 60)
print("AI RESEARCH LIBRARY")
print("=" * 60)

print(f"\nLoaded {manager.get_document_count()} papers.")

print("\nSearch by Title")
print("-" * 40)

paper = manager.search_by_title(
    "Learning to Cluster Faces via Transformer"
)
if paper:
    print(paper.summary())
else:
    print("Paper not found.")


print("\n Newest Papers")
print("-" * 40)
for document in manager.sort_by_year()[:5]:
    print(document.summary())


print("\nAlphabetical Order")
print("-" * 40)
for document in manager.sort_by_title()[:5]:
    print(document.summary())

print("\nPaper Titles")
print("-" * 40)

for title in manager.get_titles()[:5]:
    print(title)

print("\nRecent Papers")
print("-" * 40)

for paper in manager.get_recent_papers(2024):
    print(paper.summary())

print("\nEnglish Papers")
print("-" * 40)

for paper in manager.get_papers_by_language("English")[:5]:
    print(paper.summary())

print("\nGenerator Demo")
print("-" * 40)
for title in manager.iterate_titles():
    print(title)

print("\nStatistics")
print("-" * 40)
stats = manager.statistics()
for key, value in stats.items():
    print(f"{key}:{value}")

print("\nDone.")
