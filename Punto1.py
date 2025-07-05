from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title: str, item_id: int):
        if not title:
            raise ValueError("El título no debe estar vacío")
        if item_id <= 0:
            raise ValueError("ID debe ser positivo")
        
        self.title = title
        self.item_id = item_id

    @abstractmethod
    def checkout(self, user: str) -> str:
        pass

#Book
class Book(LibraryItem):
    def __init__(self, title: str, item_id: int, author: str, pages: int):
        super().__init__(title, item_id)
        if not author:
            raise ValueError("El autor no debe estar vacío")
        if pages <= 0:
            raise ValueError("La cantidad de páginas debe ser mayor a cero")
        
        self.author = author
        self.pages = pages

    def checkout(self, user: str) -> str:
        return f"Book '{self.title}' checked out by {user}."

#Magazine
class Magazine(LibraryItem):
    def __init__(self, title: str, item_id: int, issue_number: int):
        super().__init__(title, item_id)
        if issue_number <= 0:
            raise ValueError("El Número debe ser positivo")
        
        self.issue_number = issue_number

    def checkout(self, user: str) -> str:
        return f"Magazine '{self.title}' issue {self.issue_number} checked out by {user}."