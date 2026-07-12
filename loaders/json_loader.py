import json
from models.document import Document


class JsonLoader:

    """
    Loads documents from a JSON file.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> list[Document]:
        """
        Load documents from a JSON file.
        Returns:List of Document objects.
        """
        with open(self.file_path, 'r', encoding="utf_8") as file:
            data = json.load(file)
            documents = []
            for item in data:
                doc = Document(
                    id=item["id"],
                    title=item["title"],
                    author=item["author"],
                    category=item["category"],
                    pages=item["pages"],
                    language=item["language"],
                    tags=item["tags"],
                    content=item["content"],
                    year=item["year"],
                    source=item["source"],
                    pdf_url=item["pdf_url"]
                )
                documents.append(doc)
            return documents
