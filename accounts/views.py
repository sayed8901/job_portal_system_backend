# views.py in accounts app
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

from job_seeker.serializers import JobSeekerSerializer
from employer.serializers import EmployerSerializer
from .serializers import LoginSerializer

from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token


User = get_user_model()




# to get the user object data by an user_id
class UserDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        user_id = request.query_params.get('user_id')
        
        if not user_id:
            return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Depending on the user_type, use the corresponding serializer for getting the addition user data
        if user.user_type == 'employer':
            serializer = EmployerSerializer(user.employer)
        elif user.user_type == 'job_seeker':
            serializer = JobSeekerSerializer(user.job_seeker)
        else:
            return Response({'error': 'User type not supported for detailed view'}, status=status.HTTP_400_BAD_REQUEST)
        
        print(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)





# creating views for login functionality
class LoginAPIView(APIView):
    serializer_class = LoginSerializer

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
class LogoutAPIView(APIView):
    def get(self, request):
        logout(request)
        # return redirect('employer_login')
        return Response('Logout successful.')


