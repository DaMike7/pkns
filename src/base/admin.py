from django.contrib import admin
from . models import Term,Kid,Payment
# Register your models here.

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ("name","year")
    list_filter = ("year",)

@admin.register(Kid)
class KidAdmin(admin.ModelAdmin):
    list_display = ("full_name","term","kid_class")
    list_filter = ("kid_class","term",)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("amount","kid","payment_for","payment_type","paid_on")
    list_filter = ("paid_on","kid","payment_for","payment_type")

