class Book:
  def __init__(self, title: str, author: str, isbn: str):
    self.title: str = title
    self.author: str = author
    self.isbn: str = isbn
    self.is_borrowed: bool = False


class Library:
  def __init__(self):
    self.books: list[Book] = []

  def add_book(self, book: Book) -> None:
    self.books.append(book)

  def remove_book(self, isbn: str) -> None:
    self.books = [book for book in self.books if book.isbn != isbn]

  def borrow_book(self, isbn: str) -> bool:
    for book in self.books:
      if book.isbn == isbn and not book.is_borrowed:
        book.is_borrowed = True
        return True
    return False

  def return_book(self, isbn: str) -> bool:
    for book in self.books:
      if book.isbn == isbn and book.is_borrowed:
        book.is_borrowed = False
        return True
    return False

  def get_available_books(self) -> list[Book]:
    return [book for book in self.books if not book.is_borrowed]
