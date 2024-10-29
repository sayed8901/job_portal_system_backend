from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'tran_id', 'job_post', 'amount', 'currency', 'card_type', 'tran_date')


    list_filter = ('currency', 'card_type', 'tran_date')

    search_fields = ('tran_id', 'job_post__title', 'val_id', 'bank_tran_id')

    date_hierarchy = 'tran_date'

    ordering = ('-tran_date',)

    readonly_fields = ('tran_id', 'val_id', 'amount', 'currency', 'card_type', 'card_brand', 'bank_tran_id', 'tran_date', 'store_id', 'verify_sign')



admin.site.register(Payment, PaymentAdmin)