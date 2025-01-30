# Generated by Django 4.2.18 on 2025-01-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_car_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='city',
        ),
        migrations.AddField(
            model_name='office',
            name='address',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='office',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
