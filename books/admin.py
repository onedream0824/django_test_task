from django.contrib import admin
from .models import Book, Loan  # Ensure this matches the model names in models.py

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower_name', 'loan_date', 'return_date')