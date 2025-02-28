from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, LoanViewSet

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')
router.register('loans', LoanViewSet, basename='loan')

urlpatterns = [
    path('', include(router.urls)),
]