from django.shortcuts import get_object_or_404
from job_post.models import JobPost
from employer.models import Employer
from category.models import Category
from payment.models import Payment
from job_post.serializers import JobPostSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


from django.conf import settings
from django.urls import reverse
from sslcommerz_lib import SSLCOMMERZ

import random
import time


from rest_framework.permissions import IsAuthenticatedOrReadOnly
from employer.permissions import IsEmployerOrReadOnly, IsEmployerUser
from .permissions import IsOwnerOrReadOnly






"""
Generate a unique transaction ID using timestamp and a random number.
"""
def generate_unique_transaction_id():
    timestamp = int(time.time())  # Current time in seconds
    random_number = random.randint(1000, 9999)  # Random number between 1000 and 9999
    unique_id = f"{timestamp}{random_number}"  # Concatenate timestamp and random number
    return unique_id






class AllJobPostsView(APIView):
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsEmployerOrReadOnly, IsOwnerOrReadOnly]


    # to get all the posts
    def get(self, request, format = None):
        # format=None is used here to accept any types of data
        print('All PostList  --->> inside GET ')

        posts = JobPost.objects.all()
        serializer = JobPostSerializer(posts, many = True)

        return Response(serializer.data)




class PaidJobPostsView(APIView):
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsEmployerOrReadOnly, IsOwnerOrReadOnly]


    # to get all the payment completed posts
    def get(self, request, format = None):
        # format=None is used here to accept any types of data
        print('All Paid PostList  --->> inside GET ')

        paid_posts = JobPost.objects.filter(is_payment_done = True)
        serializer = JobPostSerializer(paid_posts, many = True)

        return Response(serializer.data)
    





# to publish a job post
class JobPostPublishView(APIView):
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsEmployerOrReadOnly, IsOwnerOrReadOnly]


    # to add a post
    def post(self, request, format = None):
        print('PostList  --->> inside POST ')
        print(request.data)

        serializer = JobPostSerializer(data = request.data)

        if serializer.is_valid():
            employer_id = request.query_params.get('employer_id')
            employer = get_object_or_404(Employer, id = employer_id)

            print('employer:', employer, 'user_type:', employer.user.user_type)

            serializer.save(employer = employer)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# job post detail view set
class JobPostDetailView(APIView):
    serializer_class = JobPostSerializer 

    permission_classes = [IsAuthenticatedOrReadOnly, IsEmployerOrReadOnly, IsOwnerOrReadOnly]    


    # creating a custom function to find the post object for the get(), put() or in the delete() method
    def get_object(self, pk):
        try:
            return JobPost.objects.get(pk = pk)
        except JobPost.DoesNotExist:
            raise Http404



    # get a single post
    def get(self, request, pk, format = None):
        print('inside get in post_detail')

        post = self.get_object(pk)
        serializer = JobPostSerializer(post)

        return Response(serializer.data)



    # to update a post data
    def put(self, request, pk, format = None):
        print('inside put in post_detail')
        # print('Received data:', request.data)

        post = self.get_object(pk)

        # post data ke edit & update korar jonno 'post' & request data ke die dite hobe
        serializer = JobPostSerializer(post, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        print('Validation errors:', serializer.errors)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



    # to delete a post data
    def delete(self, request, pk, format = None):
        print('inside delete in post_detail')

        post = self.get_object(pk)
        post.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)






# to get the job_posts filtered for a specific employer
class JobPostForAnEmployerAPIView(APIView):
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsEmployerOrReadOnly, IsOwnerOrReadOnly]


    def get(self, request, format=None):
        # employer = Employer.objects.get(user=request.user)

        employer_id = request.query_params.get('employer_id')
        employer = get_object_or_404(Employer, id = employer_id)

        advertisements = JobPost.objects.filter(employer = employer)
        # creating serializer with application objects
        serializer = JobPostSerializer(advertisements, many=True)

        return Response(serializer.data)






# to get all the job_posts filtered for a specific job category
class JobPostsOfJobCategoryAPIView(APIView):
    def get(self, request, format=None):
        job_category_slug = request.query_params.get('slug')
        
        if not job_category_slug:
            return Response({'error': 'Job category slug is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            category = Category.objects.get(slug=job_category_slug)
        except Category.DoesNotExist:
            return Response({'error': 'Invalid job category slug'}, status=status.HTTP_404_NOT_FOUND)
        
        job_posts = JobPost.objects.filter(
            job_category = category,
            is_payment_done = True
        )
        serializer = JobPostSerializer(job_posts, many=True)

        return Response(serializer.data)






# Creating class to initiate payment integration for a job post
class InitiatePaymentView(APIView):
    
    # Method initiate payment integration using SSLCommerz
    def initiate_ssl_payment(self, job_post):

        # SSLCommerz settings
        ssl_settings = {
            'store_id': settings.SSLCOMMERZ['store_id'],
            'store_pass': settings.SSLCOMMERZ['store_pass'],
            'issandbox': settings.SSLCOMMERZ['issandbox'],
        }

        # Create an SSLCommerz instance
        sslcz = SSLCOMMERZ(ssl_settings)

        # tran_id = generate_unique_transaction_id()
        # print(f"Generated transaction ID: {tran_id}")


        # defining payment amount based on job_post_type
        payment_amount = 0

        if job_post.job_post_type == 'standard':
            payment_amount = 1000
        elif job_post.job_post_type == 'premium':
            payment_amount = 2000
        elif job_post.job_post_type == 'hot_job':
            payment_amount = 3000


        # Payment data
        post_body = {
            'total_amount': payment_amount,
            'currency': "BDT",
            'tran_id': f"jobPost_{job_post.pk}",

            # these urls will be fetched from the url_patters file
            'success_url': self.request.build_absolute_uri(reverse('payment_success')),
            'fail_url': self.request.build_absolute_uri(reverse('payment_fail')),
            'cancel_url': self.request.build_absolute_uri(reverse('payment_cancel')),

            'cus_name': self.request.user.username,
            'cus_email': self.request.user.email,
            'cus_phone': '01915158901',
            'cus_add1': 'Narayanganj',
            'cus_city': "Dhaka",
            'cus_country': "Bangladesh",
            
            'shipping_method': 'NO',
            'product_name': job_post.job_title,
            'num_of_item': 1,
            'product_category': job_post.job_category,
            'product_profile': 'general',
        }

        # Initiate payment session
        response = sslcz.createSession(post_body) # API response

        # # print to check the response
        # print("SSLCommerz Response:", response)

        return response



    # Actual POST request
    def post(self, request):
        # Fetch job post
        job_post_id = request.query_params.get('job_post_id')
        print(job_post_id)

        if not job_post_id:
            return Response({"error": "Job post ID is required"}, status = status.HTTP_400_BAD_REQUEST)
        
        try:
            job_post = JobPost.objects.get(pk = job_post_id)
        except JobPost.DoesNotExist:
            return Response({"error": "Job post not found"}, status = status.HTTP_404_NOT_FOUND)


        # Ensure only unpaid posts can be paid for
        if job_post.is_payment_done:
            return Response({"error": "Payment already completed for this job post."}, status = status.HTTP_400_BAD_REQUEST)


        # Initiate the payment
        response = self.initiate_ssl_payment(job_post)

        if response.get('status') == 'SUCCESS':
            return Response({
                "message": "Payment initiated successfully",
                "gateway_url": response['GatewayPageURL'],
                "job_post_type": job_post.job_post_type
            })
        else:
            return Response({"error": "Failed to initiate payment"}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)






# action to define for successful payment
class PaymentSuccessView(APIView):
    def post(self, request):
        # retrieving transaction_id and validation_id
        tran_id = request.data.get('tran_id')
        val_id = request.data.get('val_id')

        print('Transaction_id:', tran_id, 'Validation_id:', val_id)
        # print(request.data)


        if tran_id and val_id:
            job_post_id = int(tran_id.split('_')[1])

            try:
                job_post = JobPost.objects.get(pk = job_post_id)

                # setting the payment completion to True
                job_post.is_payment_done = True
                
                job_post.save()



                # Save the payment information
                Payment.objects.create(
                    job_post = job_post,

                    tran_id = request.data.get('tran_id'),
                    val_id = request.data.get('val_id'),

                    amount = request.data.get('amount'),
                    currency = request.data.get('currency'),

                    card_type = request.data.get('card_type'),
                    card_brand = request.data.get('card_brand'),
                    bank_tran_id = request.data.get('bank_tran_id'),

                    store_id = request.data.get('store_id'),
                    verify_sign = request.data.get('verify_sign'),

                    tran_date = request.data.get('tran_date'),
                )


                return Response({"message": "Payment completed successfully"})
            
            except JobPost.DoesNotExist:
                return Response({"error": "Job post not found"}, status = status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Payment validation failed"}, status = status.HTTP_400_BAD_REQUEST)




# for payment failures
class PaymentFailView(APIView):
    def post(self, request):
        return Response({"message": "Payment failed, please try again."}, status=status.HTTP_400_BAD_REQUEST)




# for cancel payment
class PaymentCancelView(APIView):
    def post(self, request):
        return Response({"message": "Payment canceled by user."}, status=status.HTTP_200_OK)



