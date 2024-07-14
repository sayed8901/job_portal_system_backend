from rest_framework import serializers
from .models import JobApplication



class JobApplicationSerializer(serializers.ModelSerializer):
    # StringRelatedField for nested serializers
    job_seeker = serializers.StringRelatedField(many=False)
    # job_post = serializers.StringRelatedField(many=False)


    class Meta:
        model = JobApplication
        fields = '__all__'
        
        # # to automatically set the job_seeker based on the currently authenticated user.    # by making 'job_seeker' read_only, we dont need to provide it from the frontend 
        
        # also making "job_post" read-only for the same purpose
        read_only_fields = ["job_seeker", "job_post"]
