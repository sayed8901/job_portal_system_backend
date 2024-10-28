from django.db import models

from job_post.models import JobPost



class Payment(models.Model):
    job_post = models.OneToOneField(JobPost, on_delete=models.CASCADE, related_name="payments")

    tran_id = models.CharField(max_length=100, unique=True)
    val_id = models.CharField(max_length=100)

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)

    card_type = models.CharField(max_length=50)
    card_brand = models.CharField(max_length=50, blank=True, null=True)
    bank_tran_id = models.CharField(max_length=100, blank=True, null=True)

    store_id = models.CharField(max_length=100)
    verify_sign = models.CharField(max_length=255)

    tran_date = models.DateTimeField()



    def __str__(self):
        return f"Payment {self.tran_id} for JobPost {self.job_post.id}"

