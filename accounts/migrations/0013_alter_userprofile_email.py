# Generated by Django 5.1.6 on 2025-03-01 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_userprofile_email_alter_userprofile_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default='test@gmail.com', max_length=50),
        ),
    ]
