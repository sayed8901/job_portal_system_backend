# views.py in accounts app
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

from job_seeker.serializers import JobSeekerSerializer
from employer.serializers import EmployerSerializer

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
