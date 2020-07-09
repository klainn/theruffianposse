# Generated by Django 2.2.6 on 2020-07-09 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posse', '0031_auto_20191204_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShadowlandsClassChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('shadowlands_class', models.CharField(choices=[('TANK_DK', 'Tank Death Knight'), ('DPS_DK', 'DPS Death Knight'), ('TANK_DH', 'Tank Demon Hunter'), ('DPS_DH', 'DPS Demon Hunter'), ('TANK_DRUID', 'Tank Druid'), ('DPS_DRUID', 'DPS Druid'), ('HEALER_DRUID', 'Healer Druid'), ('HUNTER', 'Hunter'), ('MAGE', 'Mage'), ('TANK_MONK', 'Tank Monk'), ('DPS_MONK', 'DPS Monk'), ('HEALER_MONK', 'Healer Monk'), ('TANK_PALADIN', 'Tank Paladin'), ('DPS_PALADIN', 'DPS Paladin'), ('HEALER_PALADIN', 'Healer Paladin'), ('HEALER_PRIEST', 'Healer Priest'), ('DPS_PRIEST', 'DPS Priest'), ('ROGUE', 'Rogue'), ('HEALER_SHAMAN', 'Healer Shaman'), ('DPS_SHAMAN', 'DPS Shaman'), ('WARLOCK', 'Warlock'), ('TANK_WARRIOR', 'Tank Warrior'), ('DPS_WARRIOR', 'DPS Warrior')], max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Shadowlands Class Chart',
            },
        ),
    ]