# Generated by Django 4.2.4 on 2024-10-28 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_post', '0008_alter_jobpost_job_post_type'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='job_post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='job_post.jobpost'),
        ),
    ]
