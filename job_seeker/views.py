from django.shortcuts import render, redirect
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Job_seeker
from .serializers import JobSeekerSerializer, JobSeekerRegistrationSerializer, JobSeekerLoginSerializer


# necessary importing for confirmation link generating
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.utils.encoding import force_bytes

# to implement email sending functionality
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string


from accounts.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token



# Create your views here.
class JobSeekerViewSet(viewsets.ModelViewSet):
    queryset = Job_seeker.objects.all()
    serializer_class = JobSeekerSerializer




# Creating user registration functionality
class JobSeekerRegistrationAPIView(APIView):
    serializer_class = JobSeekerRegistrationSerializer

    def post(self, request):
        # form er moto kore 'serialized_data' nie nilam
        serialized_data = self.serializer_class(data = request.data)

        if serialized_data.is_valid():
            user = serialized_data.save()
            print(user)



            # creating a token for the user
            token = default_token_generator.make_token(user)
            print('token :', token)

            # creating an unique url by using the decoded string of the users unique user id such as 'pk' 
            user_id = urlsafe_base64_encode(force_bytes(user.pk))
            print('user_id :', user_id)

            # creating a confirm link
            confirm_link = f'http://127.0.0.1:8000/job_seeker/active/{user_id}/{token}/'
            


            # email sending implementation
            email_subject = 'Confirm Your Account'
            email_body = render_to_string('confirm_email.html', {
                'user': user,
                'confirm_link': confirm_link,
            })

            email = EmailMultiAlternatives(email_subject, '', to = [user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()


            return Response('Check your mail for confirmation.')


        return Response(serialized_data.errors)







# creating a function to decode the confirmation link for activating the user account
def activate(request, user_id, token):
    try:
        user_id = urlsafe_base64_decode(user_id).decode()
        user = CustomUser._default_manager.get(pk = user_id)
    except(CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('job_seeker_login')
    else:
        # er age response ba kono error message die deowa jete pare
        return redirect('job_seeker_register')





# creating views for login functionality
class JobSeekerLoginAPIView(APIView):
    serializer_class = JobSeekerLoginSerializer

    def post(self, request):
        serialized_data = self.serializer_class(data = request.data)

        if serialized_data.is_valid():
            username = serialized_data.validated_data['username']
            password = serialized_data.validated_data['password']
            user = authenticate(username = username, password = password)

            if user:
                # The method get_or_create returns a tuple containing two elements
                token, _ = Token.objects.get_or_create(user = user)
                print(token)    # getting token
                print(_)    # indicates whether the token_object was created or not
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': 'Invalid credential'})
        
        return Response(serialized_data.errors)







# creating views for logout functionality
class JobSeekerLogoutAPIView(APIView):
    def get(self, request):
        logout(request)
        return redirect('job_seeker_login')
