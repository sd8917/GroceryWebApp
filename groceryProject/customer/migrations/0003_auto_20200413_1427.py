# Generated by Django 2.2 on 2020-04-13 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20200413_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_detail',
            old_name='product_name',
            new_name='product',
        ),
    ]
