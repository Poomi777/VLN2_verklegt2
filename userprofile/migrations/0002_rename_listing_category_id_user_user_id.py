# Generated by Django 4.0.4 on 2022-05-06 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='listing_category_id',
            new_name='user_id',
        ),
    ]
