# Generated by Django 4.0.2 on 2022-03-17 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_accomodation_accomidations_sub_accomidation'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomidations',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
