# Generated by Django 5.1.6 on 2025-02-17 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_product_favorites'),
        ('products', '0006_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='product_favorites',
            field=models.ManyToManyField(blank=True, default='put your text', null=True, to='products.product'),
        ),
    ]
