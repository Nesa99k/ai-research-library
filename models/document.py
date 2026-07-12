from dataclasses import dataclass, field


@dataclass
class Document:

    """
    Represents a document in the AI Knowledge Base.
    """
    id: int
    title: str
    author: str
    category: str
    pages: int | None = None
    language: str = "English"
    tags: list[str] = field(default_factory=list)
    content: str = ""
    year: int = 0
    source: str = ""
    pdf_url: str = ""

    def word_count(self) -> int:
        """
        Returns the approximate number of words in content.
        """
        return len(self.content.split())

    # -------------------------------
    # -------------------------------

    def has_tag(self, tag: str) -> bool:
        """
         Returns True if the document contains the given tag.
        """
        return tag in self.tags

    # -------------------------------
    # --------------------------------

    def summary(self) -> str:
        """
        return: Return a short summary of the document.
        """
        return (
            f"[{self.id}] "
            f"{self.title} "
            f"({self.year}) "
            f"- {self.author}"
        )
