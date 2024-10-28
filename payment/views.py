from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import Payment
from .serializers import PaymentSerializer
from job_post.models import JobPost


from rest_framework.permissions import IsAuthenticatedOrReadOnly
from employer.permissions import IsEmployerOrReadOnly, IsEmployerUser






# Create your views here.

class AllPaymentsView(APIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsEmployerOrReadOnly]


    # to get all the payment info
    def get(self, request, format = None):
        # format=None is used here to accept any types of data
        print('All PostList  --->> inside GET ')

        posts = Payment.objects.all()
        serializer = PaymentSerializer(posts, many = True)

        return Response(serializer.data)






# payment detail view set
class PaymentOfAnJobPostByID(APIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsEmployerOrReadOnly]  


    # get a single payment
    def get(self, request, format = None):
        job_post_id = request.query_params.get('job_post_id')

        if not job_post_id:
            return Response({"error": "Job post ID is required"}, status = status.HTTP_400_BAD_REQUEST)
        
        try:
            payment_info = Payment.objects.get(job_post = job_post_id)
        except Payment.DoesNotExist:
            return Response({"error": "Job post not found"}, status = status.HTTP_404_NOT_FOUND)


        serializer = PaymentSerializer(payment_info)

        return Response(serializer.data)






# payment detail view set
class PaymentDetailView(APIView):
    serializer_class = PaymentSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, IsEmployerOrReadOnly]    


    # creating a custom function to find the payment object for the get(), put() or in the delete() method
    def get_object(self, pk):
        try:
            return Payment.objects.get(pk = pk)
        except Payment.DoesNotExist:
            raise Http404



    # get a single payment
    def get(self, request, pk, format = None):
        print('inside get in payment_detail')

        payment_data = self.get_object(pk)
        serializer = PaymentSerializer(payment_data)

        return Response(serializer.data)




    # to delete a post data
    def delete(self, request, pk, format = None):
        print('inside delete in payment_detail')

        payment_data = self.get_object(pk)
        
        # Find the associated job post
        job_post = get_object_or_404(JobPost, id = payment_data.job_post.id)
        print('job_post inside payment delete request:', job_post)
        
        # Update the job post's is_payment_done field
        job_post.is_payment_done = False
        job_post.save()

        payment_data.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)

