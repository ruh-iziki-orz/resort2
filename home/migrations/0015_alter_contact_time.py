# Generated by Django 4.0.2 on 2022-03-18 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='time',
            field=models.TimeField(auto_created=True, null=True),
        ),
    ]
