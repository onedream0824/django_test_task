from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    # Add custom related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='library_users',  # Custom related_name
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='library_users',  # Custom related_name
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)  # ISBN is unique for each book
    page_count = models.IntegerField()
    availability = models.BooleanField(default=True)  # Indicates if the book is available for loan

    def __str__(self):
        return self.title


User = get_user_model()  # Get the custom User model

class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who borrowed the book
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Book being borrowed
    borrowed_date = models.DateTimeField(auto_now_add=True)  # Date when the book was borrowed
    returned_date = models.DateTimeField(null=True, blank=True)  # Date when the book was returned (nullable)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"