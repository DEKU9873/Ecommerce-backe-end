# Generated by Django 5.1.4 on 2024-12-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_remove_product_availablecolors_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availableColors',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
