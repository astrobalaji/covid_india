# Generated by Django 2.2.5 on 2021-04-24 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='whatsapp_groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=200)),
                ('state_code', models.CharField(max_length=20)),
                ('group_url', models.CharField(max_length=2000)),
            ],
        ),
    ]
