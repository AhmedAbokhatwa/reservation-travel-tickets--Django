# Generated by Django 5.1.6 on 2025-02-18 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_userprofile_options_userprofile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
