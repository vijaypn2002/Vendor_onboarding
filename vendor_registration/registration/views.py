from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from .models import Vendor
from .forms import VendorForm
from django.core.paginator import Paginator

def vendor_registration(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = VendorForm()
    return render(request, 'registration/vendor_registration.html', {'form': form})

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Vendor

from django.shortcuts import render
from .models import Vendor
from django.core.paginator import Paginator

from django.shortcuts import render
from .models import Vendor

from django.shortcuts import render
from .models import Vendor
from django.core.paginator import Paginator
from django.http import HttpResponse
import csv

from django.shortcuts import render
from .models import Vendor
from django.core.paginator import Paginator
from django.http import HttpResponse
import csv

def vendor_list(request):
    # Get filter values from the request
    vendor_name = request.GET.get('vendor_name', '')
    vendor_type = request.GET.get('vendor_type', '')
    company_status = request.GET.get('company_status', '')
    state = request.GET.get('state', '')

    # Filter vendors based on user input
    vendors = Vendor.objects.all()

    if vendor_name:
        vendors = vendors.filter(vendor_name__icontains=vendor_name)
    if vendor_type:
        vendors = vendors.filter(vendor_type=vendor_type)
    if company_status:
        vendors = vendors.filter(company_status=company_status)
    if state:
        vendors = vendors.filter(state=state)

    # Pagination
    paginator = Paginator(vendors, 10)  # Show 10 vendors per page
    page_number = request.GET.get('page')
    vendors_page = paginator.get_page(page_number)

    # Export to CSV if the export button is pressed
    if 'export' in request.GET:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="vendors.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'Vendor Name', 'Vendor Type', 'GST No', 'PAN No', 'Company Status', 'State', 'Banking Name',
            'Bank', 'IFSC', 'Account Number', 'Address', 'STD Code with Phone No', 'Contact Person', 'City',
            'Fax', 'Contact Person Designation', 'Website', 'MSME', 'Mobile', 'Email', 'Business Description', 'Pin'
        ])

        for vendor in vendors:
            writer.writerow([
                vendor.vendor_name, vendor.vendor_type, vendor.gst_no, vendor.pan_no, vendor.company_status,
                vendor.state, vendor.banking_name, vendor.bank, vendor.ifsc, vendor.account_number, vendor.address,
                vendor.std_code_phone_no, vendor.contact_person, vendor.city, vendor.fax,
                vendor.contact_person_designation, vendor.website, vendor.is_msmse, vendor.mobile,
                vendor.email, vendor.business_description, vendor.pin
            ])

        return response

    context = {
        'vendors': vendors_page,
        'vendor_name': vendor_name,
        'vendor_type': vendor_type,
        'company_status': company_status,
        'state': state,
        'state_choices': Vendor.STATE_CHOICES,  # Pass STATE_CHOICES to the template
    }

    return render(request, 'registration/vendor_list.html', context)

import csv
from django.http import HttpResponse
from .models import Vendor
import csv
from django.http import HttpResponse
from .models import Vendor

def export_selected_vendors(request):
    vendor_ids = request.POST.getlist('selected_vendors')
    vendors = Vendor.objects.filter(id__in=vendor_ids)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="vendors.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'Vendor Name', 'Vendor Type', 'GST No', 'PAN No', 'Company Status',
        'State', 'Mobile', 'Email', 'Vendor Bank', 'Vendor IFSC',
        'Account Number', 'Address', 'Contact Person', 'Designation', 'Fax', 'Website'
    ])

    for vendor in vendors:
        writer.writerow([
            vendor.vendor_name, vendor.vendor_type, vendor.gst_no, vendor.pan_no, vendor.company_status,
            vendor.state, vendor.mobile, vendor.email, vendor.bank, vendor.ifsc,
            vendor.account_number, vendor.address, vendor.contact_person, vendor.contact_person_designation,
            vendor.fax, vendor.website
        ])

    return response


def success_page(request):
    return render(request, 'registration/success.html')
