# Generated by Django 5.0.7 on 2024-10-10 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_remove_vendor_country_remove_vendor_state_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='account_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='bank',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='banking_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='business_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='company_status',
            field=models.CharField(choices=[('Manufacturer', 'Manufacturer'), ('Authorised Dealer', 'Authorised Dealer'), ('Stockist/Trader', 'Stockist/Trader'), ('Importer/Indian Agent', 'Importer/Indian Agent'), ('Service Provider', 'Service Provider')], max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='contact_person',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='contact_person_designation',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='fax',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='gst_no',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='ifsc',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='is_msmse',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='pan_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='pin',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='state',
            field=models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='std_code_phone_no',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_type',
            field=models.CharField(choices=[('Public Limited Co', 'Public Limited Co'), ('Partnership Co', 'Partnership Co'), ('Proprietorship', 'Proprietorship'), ('Gov Sector', 'Gov Sector'), ('Others', 'Others')], max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]