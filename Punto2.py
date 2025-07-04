import csv
from Punto1 import LibraryItem, Book, Magazine  # Import del punto 1

def load_library_items(path: str) -> list[LibraryItem]:
    items = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row_num, row in enumerate(reader, start=1):
            try:
                if not row:
                    continue 

                item_type = row[0].strip().lower()

                if item_type == 'book':
                    title, item_id, author, pages = row[1], int(row[2]), row[3], int(row[4])
                    book = Book(title, item_id, author, pages)
                    items.append(book)

                elif item_type == 'magazine':
                    title, item_id, issue_number = row[1], int(row[2]), int(row[3])
                    magazine = Magazine(title, item_id, issue_number)
                    items.append(magazine)

                else:
                    print(f"[Línea {row_num}] Tipo desconocido: '{item_type}'")

            except Exception as e:
                print(f"[Línea {row_num}] Error al procesar: {row} → {e}")

    return items