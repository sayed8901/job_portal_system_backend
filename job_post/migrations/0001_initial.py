# Generated by Django 4.2.4 on 2024-07-12 20:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employer', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('job_location', models.CharField(max_length=50)),
                ('employment_status', models.CharField(choices=[('full-time', 'Full-time'), ('part-time', 'Part-time'), ('contractual', 'Contractual'), ('permanent', 'Permanent')], max_length=20)),
                ('job_context', models.TextField()),
                ('job_responsibilities', models.TextField()),
                ('education', models.TextField()),
                ('experience', models.TextField()),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18)])),
                ('vacancy', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=12)),
                ('other_benefits', models.TextField(blank=True, null=True)),
                ('date_of_job_post', models.DateField(auto_now_add=True)),
                ('deadline', models.DateField()),
                ('application_instructions', models.TextField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer', to='employer.employer')),
                ('job_category', models.ManyToManyField(related_name='job_category', to='category.category')),
            ],
        ),
    ]
