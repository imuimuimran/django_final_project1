# Generated by Django 4.2.3 on 2023-09-17 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_management', '0003_alter_book_image'),
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='wishlist_id',
        ),
        migrations.RemoveField(
            model_name='wishlistitem',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='wishlistitem',
            name='wishlist',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='books',
            field=models.ManyToManyField(related_name='wishlists', to='book_management.book'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wishlistitem',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_management.book'),
        ),
    ]