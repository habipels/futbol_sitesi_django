# Generated by Django 3.2.13 on 2022-07-31 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220731_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='club_vs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gol1', models.BigIntegerField()),
                ('gol2', models.BigIntegerField()),
                ('mac_durumu', models.BooleanField()),
                ('takim1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='takim1', to='home.clubs')),
                ('takim2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='takim2', to='home.clubs')),
            ],
        ),
    ]
