from rest_framework import serializers
from .models import JobPost



class JobPostSerializer(serializers.ModelSerializer):
    # StringRelatedField for nested serializers
    employer = serializers.StringRelatedField(many=False)
    
    # job_category = serializers.StringRelatedField(many=False)


    class Meta:
        model = JobPost
        fields = '__all__'
        
        # to automatically set the employer based on the currently authenticated user.      # by making 'employer' read_only, we dont need to provide it from the frontend form
        read_only_fields = ["employer",]
        
