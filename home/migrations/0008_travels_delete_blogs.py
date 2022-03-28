# Generated by Django 4.0.2 on 2022-03-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_hotel_info_offers_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='travels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_id', models.CharField(auto_created=True, max_length=50, unique=True)),
                ('auther', models.CharField(blank=True, max_length=50)),
                ('cover', models.ImageField(upload_to='travels')),
                ('image', models.ImageField(upload_to='travels')),
                ('summary', models.TextField(blank=True)),
                ('sub_summary', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Blogs',
        ),
    ]