from rest_framework import serializers
from .models import Book, Loan
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['id', 'book', 'borrowed_date', 'return_date']
        read_only_fields = ['borrowed_date', 'return_date']
    
    def create(self, validated_data):
        book = validated_data['book']
        if not book.is_available:
            raise serializers.ValidationError({"book": "This book is not available."})
        
        book.is_available = False
        book.save()
        
        loan = Loan.objects.create(
            user=self.context['request'].user,
            **validated_data
        )
        return loan

class ReturnBookSerializer(serializers.Serializer):
    loan_id = serializers.IntegerField()
    
    def validate_loan_id(self, value):
        try:
            loan = Loan.objects.get(id=value, return_date=None)
        except Loan.DoesNotExist:
            raise serializers.ValidationError("Invalid loan ID or book already returned.")
        return value
    
    def save(self):
        loan = Loan.objects.get(id=self.validated_data['loan_id'])
        loan.return_date = timezone.now()
        loan.save()
        
        book = loan.book
        book.is_available = True
        book.save()
        
        return loan