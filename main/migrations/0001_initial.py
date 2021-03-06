# Generated by Django 4.0.3 on 2022-03-21 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=15)),
                ('open_price', models.FloatField(blank=True, null=True)),
                ('close_price', models.FloatField(blank=True, null=True)),
                ('upper_circuit', models.FloatField(blank=True, null=True)),
                ('lower_circuit', models.FloatField(blank=True, null=True)),
                ('registered_at', models.CharField(blank=True, choices=[('nse', 'nse'), ('bse', 'bse')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(default='', max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('username', models.CharField(max_length=56, unique=True)),
                ('email', models.EmailField(blank=True, max_length=155, null=True)),
                ('profile_pic', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stockdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('video', models.SlugField(blank=True, null=True)),
                ('detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.stock')),
            ],
        ),
    ]
