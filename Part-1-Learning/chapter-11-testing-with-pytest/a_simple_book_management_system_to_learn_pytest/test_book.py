from book import Book
import pytest

@pytest.fixture
def book():
    book = Book("Harry Potter", "JK Rowling", 150)
    return book

def test_book_is_available(book):
    assert book.is_available() == True

def test_book_borrow(book): 
    prev = book.copy
    temp = book.borrow(book.name)
    assert temp < prev

def test_book_return(book):
    prev = book.copy
    temp = book.return_book(book.name)
    assert temp > prev
