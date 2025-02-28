from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, LoanViewSet, UserRegistrationView

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'loans', LoanViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('books/', BookViewSet.as_view(), name='books'),
    path('loans/', LoanViewSet.as_view(), name='loans'),
    path('', include(router.urls)),
]