from django.contrib import admin
from .models import Book, Loan

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'is_available')
    list_filter = ('is_available', 'author')
    search_fields = ('title', 'author', 'isbn')

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrowed_date', 'return_date')
    list_filter = ('borrowed_date', 'return_date')
    search_fields = ('user__username', 'book__title')