from django.contrib import admin
from .models import Book, Loan

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'availability')

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrowed_date', 'returned_date')