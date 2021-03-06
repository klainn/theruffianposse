# Generated by Django 2.2.6 on 2019-10-26 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posse', '0005_raideriosettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_created=True)),
                ('news_description', models.CharField(max_length=255)),
                ('news_body', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Guild News and Updates',
            },
        ),
    ]
