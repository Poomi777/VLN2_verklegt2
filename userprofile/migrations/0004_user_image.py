# Generated by Django 4.0.4 on 2022-05-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_remove_user_category_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.CharField(default='https://d25tv1xepz39hi.cloudfront.net/2016-07-16/files/cat-sample_1313.jpg', max_length=500),
        ),
    ]
