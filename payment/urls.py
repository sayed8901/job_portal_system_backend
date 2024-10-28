from django.urls import path, include

from .views import AllPaymentsView, PaymentDetailView, PaymentOfAnJobPostByID


urlpatterns = [
    path("all/", AllPaymentsView.as_view(), name="payment_list"),

    path("all/<int:pk>/", PaymentDetailView.as_view(), name="payment_detail"),

    path("by_job_post_id/", PaymentOfAnJobPostByID.as_view(), name="payment_detail_by_Job_post_id"),
]


