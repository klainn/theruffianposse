# Generated by Django 2.2.6 on 2019-11-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posse', '0027_guildleadership'),
    ]

    operations = [
        migrations.AddField(
            model_name='guildleadership',
            name='character_realm',
            field=models.CharField(default='None', max_length=100),
            preserve_default=False,
        ),
    ]