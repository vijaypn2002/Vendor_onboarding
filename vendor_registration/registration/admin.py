from django.contrib import admin
from .models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_name', 'gst_no', 'pan_no', 'banking_name', 'email']
    search_fields = ['vendor_name', 'gst_no', 'pan_no']
