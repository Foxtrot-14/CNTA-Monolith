# Generated by Django 4.1.3 on 2022-11-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_child_adder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='fName',
            field=models.CharField(max_length=20, null=True),
        ),
    ]