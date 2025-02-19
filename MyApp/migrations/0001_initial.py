# Generated by Django 4.2.18 on 2025-01-30 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=150)),
                ('car_desc', models.TextField()),
                ('transmission', models.CharField(max_length=50)),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mileage', models.IntegerField()),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='car/images/')),
                ('cost_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('email', models.CharField(default='', max_length=150)),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('message', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_field', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=90)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=500)),
                ('city', models.CharField(default='', max_length=50)),
                ('days_for_rent', models.IntegerField(default=0)),
                ('date', models.DateField(blank=True, null=True)),
                ('loc_from', models.CharField(default='', max_length=50)),
                ('loc_to', models.CharField(default='', max_length=50)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MyApp.car')),
            ],
        ),
    ]
