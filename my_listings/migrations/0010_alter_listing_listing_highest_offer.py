# Generated by Django 4.0.4 on 2022-05-13 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_listings', '0009_alter_listing_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_highest_offer',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
