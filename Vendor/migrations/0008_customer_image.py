# Generated by Django 3.2 on 2021-04-25 14:18

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0007_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=cloudinary.models.CloudinaryField(default='../static/images/default.jpg', max_length=255, null=True, verbose_name='image'),
        ),
    ]
