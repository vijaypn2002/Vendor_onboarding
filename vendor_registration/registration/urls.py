from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.vendor_registration, name='vendor_registration'),
    path('vendor-list/', views.vendor_list, name='vendor_list'),
    path('export-vendors/', views.export_selected_vendors, name='export_selected_vendors'),
    path('success/', views.success_page, name='success_page'),
]
