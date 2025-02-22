# Generated by Django 5.1.6 on 2025-02-18 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_userprofile_product_favorites'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['user'], 'verbose_name': 'Pofile for user sign in'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
