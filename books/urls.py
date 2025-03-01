from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, LoanViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('loans', LoanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]