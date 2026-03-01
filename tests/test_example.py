import unittest

from example.example import Book, Library


class TestLibrary(unittest.TestCase):
  def setUp(self) -> None:
    self.library = Library()
    self.sample_book = Book(
      "The Great Gatsby",
      "F. Scott Fitzgerald",
      "9780743273565",
    )

  def test_add_book(self) -> None:
    self.library.add_book(self.sample_book)
    self.assertEqual(len(self.library.books), 1)
    self.assertEqual(
      self.library.books[0].title,
      "The Great Gatsby",
    )

  def test_remove_book(self) -> None:
    self.library.add_book(self.sample_book)
    self.library.remove_book("9780743273565")
    self.assertEqual(len(self.library.books), 0)

  def test_borrow_book(self) -> None:
    self.library.add_book(self.sample_book)
    self.assertTrue(self.library.borrow_book("9780743273565"))
    self.assertTrue(self.sample_book.is_borrowed)
    self.assertFalse(self.library.borrow_book("9780743273565"))

  def test_return_book(self) -> None:
    self.library.add_book(self.sample_book)
    self.library.borrow_book("9780743273565")
    self.assertTrue(self.library.return_book("9780743273565"))
    self.assertFalse(self.sample_book.is_borrowed)
    self.assertFalse(self.library.return_book("9780743273565"))

  def test_get_available_books(self) -> None:
    self.library.add_book(self.sample_book)
    self.library.add_book(
      Book(
        "To Kill a Mockingbird",
        "Harper Lee",
        "9780446310789",
      )
    )
    self.library.borrow_book("9780743273565")
    available_books = self.library.get_available_books()
    self.assertEqual(len(available_books), 1)
    self.assertEqual(
      available_books[0].title,
      "To Kill a Mockingbird",
    )
