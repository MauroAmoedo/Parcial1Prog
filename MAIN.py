from Punto2 import load_library_items
from Punto3 import checkout_items, count_items, find_by_title

def main():
    items = load_library_items("library.csv") 

    print(" [Items cargados]")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item.__class__.__name__}: {item.title}")

    print(" [Checkout] ")
    for msg in checkout_items(items, "Mauro"):
        print(msg)

    print(" [Conteo] ")
    print(count_items(items))

    print(" [Busqueda de Star Wars] ")
    for item in find_by_title(items, "Star Wars"):
        print(f"- {item.title} ({item.__class__.__name__})")



if __name__ == "__main__":
    main()