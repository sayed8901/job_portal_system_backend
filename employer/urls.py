from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployerViewSet, EmployerRegistrationAPIView, activate


# Create a router
router = DefaultRouter()

# register ViewSets with the router.
router.register('list', EmployerViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('register/', EmployerRegistrationAPIView.as_view(), name='employer_register'),
    path('active/<user_id>/<token>/', activate, name='employer_account_activate'),
]

