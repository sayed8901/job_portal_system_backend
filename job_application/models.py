from django.db import models

from job_seeker.models import Job_seeker
from job_post.models import JobPost

from django.core import validators



# Create your models here.
class JobApplication(models.Model):
    job_seeker = models.ForeignKey(Job_seeker, on_delete=models.CASCADE, related_name='applicant')

    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='advertisement')

    # temporarily disabled for vercel deployment purpose
    # resume = models.FileField(upload_to='job_application/media/applications/', validators=[
    #     validators.FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf'], 
    #     message='File type must be in pdf, doc or docx format.')
    # ])

    salary = models.IntegerField()

    applied_on = models.DateField(auto_now_add=True)



    def __str__(self):
        return f'${self.job_seeker.user.username} applied to: ${self.job_post.job_title} on ${self.applied_on}.'

