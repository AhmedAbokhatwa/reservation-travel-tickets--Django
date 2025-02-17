# Generated by Django 5.1.6 on 2025-02-17 18:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_options_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(default=datetime.datetime.now)),
                ('name', models.CharField(max_length=50, verbose_name='Category Name')),
            ],
            options={
                'verbose_name': 'Category NAME',
                'ordering': ['name'],
            },
        ),
    ]
