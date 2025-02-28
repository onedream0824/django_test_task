from rest_framework import serializers
from .models import User, Book, Loan

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_admin']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
    fields = '__all__'


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
    fields = '__all__'