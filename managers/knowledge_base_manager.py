from models.document import Document


class KnowledgeBaseManager:
    """
    Manages a collection of Document objects.
    """

    def __init__(self):
        self.documents: list[Document] = []

    def add_document(self, document: Document) -> None:
        """
        Add a new document to the knowledge base.
        """
        self.documents.append(document)

    def get_document_count(self) -> int:
        return len(self.documents)

# _________________________________________
# Search_by_title
# _________________________________________

    def search_by_title(self, title: str) -> Document | None:
        """
         Search for a document by its exact title.
          Returns:
          Document if found, otherwise None.

        """
        for document in self.documents:
            if document.title.lower() == title.lower():
                return document
        return None
# ________________________________________
# Delete
# ________________________________________

    def remove_document(self, document_id: int) -> bool:
        """
    Remove a document by its id.

    Returns:
        True if removed successfully.
        False otherwise.
    """
        for document in self.documents:
            if document.id == document_id:
                self.documents.remove(document)
                return True
        return False

# _________________________________________
# search_by_tag
# _________________________________________

    def search_by_tag(self, tag: str) -> list[Document]:
        return [
            document
            for document in self.documents
            if document.has_tag(tag)
        ]

# ________________________________________
# search_by_category
# ________________________________________

    def search_by_category(self, category: str) -> list[Document]:

        return [
            document for document in self.documents if document.category.lower() == category.lower()
        ]

# ________________________________________
# sort_by_title
# ________________________________________

    def sort_by_title(self) -> list[Document]:
        """
        Return all documents sorted alphabetically by title.
        """
        return sorted(
            self.documents,
            key=lambda document: document.title.lower()
        )

    def sort_by_year(self) -> list[Document]:
        """
        Return documents sorted from newest to oldest.
        """
        return sorted(
            self.documents,
            key=lambda document: document.year,
            reverse=True
        )

    def sort_by_pages(self) -> list[Document]:
        """
        Return documents sorted by page count.
        Unknown page counts appear last.
        """
        return sorted(
            self.documents,
            key=lambda document: (
                document.pages is None,
                document.pages if document.pages is not None else 0
            )
        )
# ----------------- map ---------------------------

    def get_titles(self) -> list[str]:
        """
        Return titles of all documents.
        """
        return list(
            map(
                lambda document: document.title,
                self.documents
            )
        )

    def get_authors(self) -> list[str]:
        """
        Return authors of all documents.
        """
        return list(
            map(
                lambda document: document.author,
                self.documents
            )
        )

    def get_categories(self) -> list[str]:
        """
        Return categories of all documents.
        """
        return list(
            map(
                lambda document: document.category,
                self.documents
            )
        )
# ----------------- filter ---------------------------

    def get_recent_papers(self, year: int) -> list[Document]:
        """
        Return papers published from the given year onward.
        """
        return list(
            filter(
                lambda document: document.year >= year,
                self.documents
            )
        )

    def get_papers_by_language(self, language: str) -> list[Document]:
        """
        Return papers written in the given language.
        """
        return list(
            filter(
                lambda document: document.language.lower() == language.lower(),
                self.documents
            )
        )

    def get_llm_papers(self) -> list[Document]:
        """
        Return papers related to Large Language Models.
        """
        return list(
            filter(
                lambda document: "large language model" in document.title.lower()
                or any(
                    "llm" in tag.lower()
                    or "language" in tag.lower()
                    for tag in document.tags
                ),
                self.documents
            )
        )
# ---------------- Generator --------------------

    def iterate_titles(self):
        """
        Yield document titles one by one.
        """
        for document in self.documents:
            yield document.title

    def iterate_documents(self):
        """
        Yield documents one by one.
        """
        for document in self.documents:
            yield document

# -------------- Statistics -----------------------

    def statistics(self) -> dict[str, int]:
        """
        Return basic statistics about the library.
        """
        return {
            "documents": len(self.documents),

            "categories": len(
                set(
                    document.category
                    for document in self.documents
                )
            ),

            "languages": len(
                set(
                    document.language
                    for document in self.documents
                )
            ),

            "newest_year": max(
                document.year
                for document in self.documents
            )
        }
