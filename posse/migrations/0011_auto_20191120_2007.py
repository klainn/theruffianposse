# Generated by Django 2.2.7 on 2019-11-20 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posse', '0010_guildapplications_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guildapplications',
            name='application_status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Denied', 'Denied'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
    ]
