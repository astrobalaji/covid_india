# Generated by Django 2.2.5 on 2021-04-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_ser',
            name='Area',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='food_ser',
            name='City',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='food_ser',
            name='Delivery',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='food_ser',
            name='Hours',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='food_ser',
            name='Name',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='food_ser',
            name='Number',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='food_ser',
            name='Service',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='food_ser',
            name='Social',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='food_ser',
            name='State',
            field=models.CharField(max_length=2000),
        ),
    ]
