# Generated by Django 4.1.2 on 2022-10-20 03:27

import datetime
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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='categories/')),
                ('content', models.TextField(default=None, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('active', models.BooleanField(default=True, help_text='Open - close status post with user', verbose_name='post status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'catalog_category',
                'verbose_name_plural': 'catalog_categories',
                'db_table': 'catalog_category',
                'ordering': ['created_at', 'title'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(default=None, max_length=100, null=True)),
                ('p_code', models.CharField(max_length=50, unique=True)),
                ('p_image', models.ImageField(blank=True, default=None, null=True, upload_to='products/')),
                ('p_description', models.TextField(blank=True, default=None, max_length=1000, null=True)),
                ('p_country', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('active', models.BooleanField(default=True, help_text='Open - close status post with user', verbose_name='post status')),
                ('categories', models.ManyToManyField(related_name='catalog_products', to='catalog_app.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'catalog_product',
                'verbose_name_plural': 'catalog_products',
                'db_table': 'catalog_product',
                'ordering': ['created_at', 'p_name'],
                'managed': True,
            },
        ),
    ]