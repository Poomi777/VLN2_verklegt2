# Generated by Django 4.0.4 on 2022-05-06 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('street_name', models.CharField(max_length=30)),
                ('apartment_number', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('postal_code', models.IntegerField()),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.user')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardholder_name', models.CharField(max_length=30)),
                ('card_number', models.IntegerField()),
                ('month_expiration', models.IntegerField()),
                ('year_expiration', models.IntegerField()),
                ('cvc', models.IntegerField()),
                ('cart_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.cart')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.user')),
            ],
        ),
    ]
