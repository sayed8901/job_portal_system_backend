from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('job_seeker/', include('job_seeker.urls')),
    path('employer/', include('employer.urls')),
    path('category/', include('category.urls')),
    path('job_posts/', include('job_post.urls')),
    path('job_applications/', include('job_application.urls')),
    path('payment/', include('payment.urls')),
    
    # to implement authentication facility only in DRF panel
    path("api-auth/", include("rest_framework.urls")),
]

# adding onto the urlpatterns
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
