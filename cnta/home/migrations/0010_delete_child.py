# Generated by Django 4.1.3 on 2022-11-29 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_child_fname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Child',
        ),
    ]