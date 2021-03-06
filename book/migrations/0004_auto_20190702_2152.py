# Generated by Django 2.2.3 on 2019-07-03 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20190702_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='author_book',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='name_book',
        ),
        migrations.RenameField(
            model_name='rentbook',
            old_name='user',
            new_name='librarian',
        ),
        migrations.AddField(
            model_name='rentbook',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
