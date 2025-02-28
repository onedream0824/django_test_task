from rest_framework import viewsets, filters, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


from .models import Book, Loan
from .serializers import BookSerializer, LoanSerializer, ReturnBookSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_admin

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'is_available']
    search_fields = ['title', 'author', 'isbn']
    ordering_fields = ['title', 'author', 'publication_date']

class LoanViewSet(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            return Loan.objects.all()
        return Loan.objects.filter(user=user)
    
    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['post'])
    def return_book(self, request):
        serializer = ReturnBookSerializer(data=request.data)
        if serializer.is_valid():
            loan = serializer.save()
            return Response({'message': f'Book {loan.book.title} returned successfully.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)