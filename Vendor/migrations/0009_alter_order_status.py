# Generated by Django 3.2 on 2021-04-25 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0008_customer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], default='Pending', max_length=200, null=True),
        ),
    ]
