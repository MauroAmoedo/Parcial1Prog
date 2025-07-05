import unittest
from Punto1 import Book, Magazine
from Punto2 import load_library_items
from Punto3 import checkout_items, count_items, find_by_title
import tempfile
import os

class TestBiblioteca(unittest.TestCase):

    def test_constructor_book_valido(self):
        book = Book("Dune", 1, "Frank Herbert", 688)
        self.assertEqual(book.title, "Dune")
        self.assertEqual(book.pages, 688)

    def test_constructor_book_invalido(self):
        with self.assertRaises(ValueError):
            Book("", 1, "Autor", 200)
        with self.assertRaises(ValueError):
            Book("Título", -5, "Autor", 200)
        with self.assertRaises(ValueError):
            Book("Título", 1, "", 200)
        with self.assertRaises(ValueError):
            Book("Título", 1, "Autor", -10)

    def test_constructor_magazine_valido(self):
        mag = Magazine("Forbes", 2, 305)
        self.assertEqual(mag.issue_number, 305)

    def test_constructor_magazine_invalido(self):
        with self.assertRaises(ValueError):
            Magazine("", 2, 128)
        with self.assertRaises(ValueError):
            Magazine("Revista", 0, 128)
        with self.assertRaises(ValueError):
            Magazine("Revista", 2, -1)

    def test_checkout_book(self):
        book = Book("Star Wars: Thrawn", 1, "Timothy Zahn", 420)
        self.assertEqual(book.checkout("Mauro"), "Book 'Star Wars: Thrawn' checked out by Mauro.")

    def test_checkout_magazine(self):
        mag = Magazine("Caras", 2, 1234)
        self.assertEqual(mag.checkout("Mauro"), "Magazine 'Caras' issue 1234 checked out by Mauro.")

    def test_load_library_items(self):
        contenido = (
            "book,Star Wars: Thrawn,1,Timothy Zahn,420\n"
            "book,Dune,2,Frank Herbert,688\n"
            "book,Ubik,3,Philip K. Dick,256\n"
            "magazine,Forbes,4,305\n"
            "magazine,Caras,5,1234\n"
            "magazine,Noticias,6,980\n"
            "book,Error,-1,Autor X,123\n" 
        )
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
            tmp.write(contenido)
            tmp_path = tmp.name

        items = load_library_items(tmp_path)
        os.remove(tmp_path)

        self.assertEqual(len(items), 6)
        self.assertIsInstance(items[0], Book)
        self.assertIsInstance(items[3], Magazine)

    def test_checkout_items(self):
        items = [
            Book("Dune", 1, "Frank Herbert", 688),
            Magazine("Noticias", 2, 980)
        ]
        mensajes = checkout_items(items, "Mauro")
        self.assertIn("Book 'Dune' checked out by Mauro.", mensajes)
        self.assertIn("Magazine 'Noticias' issue 980 checked out by Mauro.", mensajes)

    def test_count_items(self):
        items = [
            Book("Dune", 1, "Frank Herbert", 688),
            Book("Ubik", 2, "Philip K. Dick", 256),
            Magazine("Caras", 3, 1234)
        ]
        counts = count_items(items)
        self.assertEqual(counts, {"book": 2, "magazine": 1})

    def test_find_by_title(self):
        items = [
            Book("Star Wars: Thrawn", 1, "Timothy Zahn", 420),
            Magazine("Noticias", 2, 980),
            Book("Do Androids Dream of Electric Sheep?", 3, "Philip K. Dick", 210)
        ]
        resultados = find_by_title(items, "star wars")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].title, "Star Wars: Thrawn")

if __name__ == '__main__':
    unittest.main()
