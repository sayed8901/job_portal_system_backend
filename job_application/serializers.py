from rest_framework import serializers
from .models import JobApplication
from job_seeker.models import Job_seeker



class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_seeker
        fields = ['fathers_name', 'mothers_name', 'address', 'contact_no', 'sex', 'age', 'education', 'experience', ]



class JobApplicationSerializer(serializers.ModelSerializer):
    # StringRelatedField for nested serializers, to only show the user name, not the whole job_seeker object data
    # job_seeker = serializers.StringRelatedField(many=False)
    
    # to see the full detail of job_seeker
    job_seeker = JobSeekerSerializer(read_only=True)

    # job_post = serializers.StringRelatedField(many=False)


    class Meta:
        model = JobApplication
        fields = '__all__'
        
        # # to automatically set the job_seeker based on the currently authenticated user.    # by making 'job_seeker' read_only, we dont need to provide it from the frontend 
        
        # also making "job_post" read-only for the same purpose
        read_only_fields = ["job_seeker", "job_post"]

