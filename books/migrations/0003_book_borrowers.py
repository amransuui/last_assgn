# Generated by Django 4.2.7 on 2023-12-29 16:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0002_comment_user_alter_book_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrowers',
            field=models.ManyToManyField(blank=True, related_name='borrowed_books', to=settings.AUTH_USER_MODEL),
        ),
    ]
