# Generated by Django 3.2 on 2021-05-04 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_short'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short',
            field=models.TextField(blank=True, default='short description'),
        ),
    ]