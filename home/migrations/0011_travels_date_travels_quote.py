# Generated by Django 4.0.2 on 2022-03-18 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_contact_quote_phone_no_quote_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='travels',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='travels',
            name='quote',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
