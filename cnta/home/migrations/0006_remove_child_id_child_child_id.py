# Generated by Django 4.1.3 on 2022-11-27 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_child_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='id',
        ),
        migrations.AddField(
            model_name='child',
            name='child_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
