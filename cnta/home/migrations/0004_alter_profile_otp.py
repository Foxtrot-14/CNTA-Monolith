# Generated by Django 4.1.3 on 2022-11-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_profile_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='otp',
            field=models.CharField(max_length=6),
        ),
    ]
