# Generated by Django 5.0 on 2024-01-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'PENDING'), ('C', 'CANCLED'), ('CP', 'COMPLETED'), ('CF', 'CONFIRMED')], default='P', max_length=2),
        ),
    ]
