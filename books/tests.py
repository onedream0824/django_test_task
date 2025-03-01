from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Author Name",
            isbn="1234567890123",
            page_count=100,
            availability=True,
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")