# Generated by Django 4.0.2 on 2022-03-27 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_hotel_infos_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='quote',
            name='date_of_travel',
        ),
        migrations.AddField(
            model_name='quote',
            name='fromDate',
            field=models.DateField(null=True, verbose_name='from Date'),
        ),
        migrations.AddField(
            model_name='quote',
            name='toDate',
            field=models.DateField(null=True, verbose_name='to Date'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='budget',
            field=models.CharField(max_length=50, null=True, verbose_name='budget'),
        ),
    ]
