from django.urls import path, include


# Importing view classes for the job posts and payment handling
from .views import (
    AllJobPostsView,
    PaidJobPostsView,
    JobPostPublishView,
    JobPostDetailView,
    JobPostForAnEmployerAPIView,
    JobPostsOfJobCategoryAPIView,
    InitiatePaymentView,
    PaymentSuccessView,
    PaymentFailView,
    PaymentCancelView,
)



urlpatterns = [
    # Route to fetch all job posts
    path("all/", AllJobPostsView.as_view(), name="post_list"),
    
    # Route to fetch all paid job posts
    path("all_paid/", PaidJobPostsView.as_view(), name="paid_posts"),


    # Route to fetch details of a specific job post by primary key (pk)
    path("all/<int:pk>/", JobPostDetailView.as_view(), name="post_detail"),



    # Route to initiate payment for a specific job post identified by its id
    path("payment/initiate/", InitiatePaymentView.as_view(), name="initiate_payment"),


    # Route for handling successful payment notifications
    path('payment/success/', PaymentSuccessView.as_view(), name='payment_success'),

    # Route for handling failed payment notifications
    path("payment/fail/", PaymentFailView.as_view(), name="payment_fail"),

    # Route for handling canceled payment actions
    path("payment/cancel/", PaymentCancelView.as_view(), name="payment_cancel"),



    # Route to publish a new job post
    path("publish/", JobPostPublishView.as_view(), name="publish_post"),



    # Route to fetch job posts created by the logged-in employer
    path('my_advertisements/', JobPostForAnEmployerAPIView.as_view(), name='my_advertisements'),

    # Route to fetch job posts of a specific category
    path('job_posts_of_a_category/', JobPostsOfJobCategoryAPIView.as_view(), name='job_posts_of_a_category'),
]

