# Generated by Django 4.0.4 on 2022-05-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListingCategory',
            fields=[
                ('listing_category_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category_link', models.CharField(max_length=500)),
            ],
        ),
    ]
