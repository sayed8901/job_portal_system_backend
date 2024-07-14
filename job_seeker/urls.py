from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobSeekerViewSet, JobSeekerRegistrationAPIView, activate, JobSeekerLoginAPIView, JobSeekerLogoutAPIView


# Create a router
router = DefaultRouter()
# register ViewSets with the router.
router.register('list', JobSeekerViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('register/', JobSeekerRegistrationAPIView.as_view(), name='job_seeker_register'),
    path('login/', JobSeekerLoginAPIView.as_view(), name='job_seeker_login'),
    path('logout/', JobSeekerLogoutAPIView.as_view(), name='job_seeker_logout'),
    path('active/<user_id>/<token>/', activate, name='job_seeker_account_activate'),
]
