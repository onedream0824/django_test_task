from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Loan
from users.models import User
import datetime

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            isbn="1234567890123",
            page_count=200,
            publication_date=datetime.date.today()
        )
    
    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertTrue(self.book.is_available)

class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_user(
            username='admin', 
            password='adminpass',
            is_admin=True
        )
        self.regular_user = User.objects.create_user(
            username='user', 
            password='userpass'
        )
        self.book = Book.objects.create(
            title="API Test Book",
            author="API Test Author",
            isbn="9876543210123",
            page_count=300,
            publication_date=datetime.date.today()
        )
    
    def test_anonymous_can_list_books(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_anonymous_cannot_create_book(self):
        book_data = {
            'title': 'New Book',
            'author': 'New Author',
            'isbn': '1111222233334',
            'page_count': 250,
            'publication_date': datetime.date.today().isoformat()
        }
        response = self.client.post(reverse('book-list'), book_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_admin_can_create_book(self):
        self.client.force_authenticate(user=self.admin_user)
        book_data = {
            'title': 'Admin Book',
            'author': 'Admin Author',
            'isbn': '5555666677778',
            'page_count': 350,
            'publication_date': datetime.date.today().isoformat()
        }
        response = self.client.post(reverse('book-list'), book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_regular_user_can_borrow_book(self):
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post(reverse('loan-list'), {'book': self.book.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verify book is no longer available
        self.book.refresh_from_db()
        self.assertFalse(self.book.is_available)