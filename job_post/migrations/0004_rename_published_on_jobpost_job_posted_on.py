# Generated by Django 4.2.4 on 2024-07-13 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_post', '0003_jobpost_delete_job_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpost',
            old_name='published_on',
            new_name='job_posted_on',
        ),
    ]
