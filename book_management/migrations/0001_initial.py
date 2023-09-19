# Generated by Django 4.2.3 on 2023-09-14 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('isbn', models.CharField(max_length=13)),
                ('image', models.ImageField(upload_to='photos/products')),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('genre', models.CharField(max_length=100)),
                ('availability_status', models.BooleanField(default=True)),
                ('no_of_books_available', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
