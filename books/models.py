from django.db import models

class Book(models.Model):
    # Fields for the Book model
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

class Loan(models.Model):
    # Fields for the Loan model
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=255)
    loan_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)