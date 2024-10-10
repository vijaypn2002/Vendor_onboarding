from django.db import models

class Vendor(models.Model):
    FIRM_TYPE_CHOICES = [
        ('Public Limited Co', 'Public Limited Co'),
        ('Partnership Co', 'Partnership Co'),
        ('Proprietorship', 'Proprietorship'),
        ('Gov Sector', 'Gov Sector'),
        ('Others', 'Others'),
    ]

    COMPANY_STATUS_CHOICES = [
        ('Manufacturer', 'Manufacturer'),
        ('Authorised Dealer', 'Authorised Dealer'),
        ('Stockist/Trader', 'Stockist/Trader'),
        ('Importer/Indian Agent', 'Importer/Indian Agent'),
        ('Service Provider', 'Service Provider'),
    ]

    STATE_CHOICES = [
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
    ]

    # Company Details
    vendor_name = models.CharField(max_length=255)
    vendor_type = models.CharField(max_length=50, choices=FIRM_TYPE_CHOICES)
    gst_no = models.CharField(max_length=15)
    pan_no = models.CharField(max_length=10)
    company_status = models.CharField(max_length=50, choices=COMPANY_STATUS_CHOICES)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    banking_name = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    ifsc = models.CharField(max_length=11)
    account_number = models.CharField(max_length=20)

    # Vendor Contact Information
    address = models.TextField()
    std_code_phone_no = models.CharField(max_length=20)
    contact_person = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    fax = models.CharField(max_length=20, blank=True, null=True)
    contact_person_designation = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)  # Making website optional (non-mandatory)
    is_msmse = models.CharField(
        max_length=3,
        choices=[('Yes', 'Yes'), ('No', 'No')],
        default='No',
    )
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    business_description = models.TextField()
    pin = models.CharField(max_length=10)

    def __str__(self):
        return self.vendor_name
