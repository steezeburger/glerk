# Generated by Django 5.0.2 on 2024-08-31 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_cover_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
