# Generated by Django 4.0.2 on 2022-03-18 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_travels_date_travels_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='last_name',
        ),
        migrations.AddField(
            model_name='quote',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='title',
            field=models.CharField(max_length=30, null=True, verbose_name='Title'),
        ),
    ]
