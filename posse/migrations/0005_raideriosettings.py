# Generated by Django 2.2.6 on 2019-10-26 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posse', '0004_auto_20191025_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaiderIOSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Raider.IO Settings',
            },
        ),
    ]
