# Generated by Django 4.0.2 on 2022-03-17 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='offer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.offers', verbose_name='offer'),
        ),
        migrations.AlterField(
            model_name='accomidations_sub',
            name='facilities',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='accomidations_sub',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='assests/rooms'),
        ),
        migrations.AlterField(
            model_name='accomidations_sub',
            name='room_view',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='accomidations_sub',
            name='rooms',
            field=models.IntegerField(blank=True, null=True, verbose_name='no of rooms'),
        ),
    ]
