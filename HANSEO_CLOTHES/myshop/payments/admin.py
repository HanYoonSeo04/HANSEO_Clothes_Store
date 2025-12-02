from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "user", "depositor_name", "is_confirmed", "created_at")
    list_editable = ("is_confirmed",)
