# Generated by Django 3.2.25 on 2024-06-10 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_rename_shiping_cost_order_shipping_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='line_item_total',
            new_name='lineitem_total',
        ),
    ]
