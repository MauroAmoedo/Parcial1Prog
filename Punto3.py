from Punto1 import LibraryItem, Book, Magazine

def checkout_items(items: list[LibraryItem], user: str) -> list[str]:
    """
    Aplica checkout(user) y devuelve los mensajes.
    """
    return [item.checkout(user) for item in items]

def count_items(items: list[LibraryItem]) -> dict:
    """
    conteo por tipo.
    """
    counts = {"book": 0, "magazine": 0}
    for item in items:
        if isinstance(item, Book):
            counts["book"] += 1
        elif isinstance(item, Magazine):
            counts["magazine"] += 1
    return counts

def find_by_title(items: list[LibraryItem], keyword: str) -> list[LibraryItem]:
    """
    Devuelve ítems si el título contiene la palabra clave.
    """
    keyword_lower = keyword.lower()
    return [item for item in items if keyword_lower in item.title.lower()]