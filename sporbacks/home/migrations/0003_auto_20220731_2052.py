# Generated by Django 3.2.13 on 2022-07-31 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_clubs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubs',
            name='takim_logo',
            field=models.ImageField(blank=True, default='takim_resim/mnc.png', null=True, upload_to='takim_resim/', verbose_name='Takım Resimi'),
        ),
        migrations.CreateModel(
            name='club_point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.BigIntegerField()),
                ('win', models.BigIntegerField()),
                ('loss', models.BigIntegerField()),
                ('takim', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.clubs')),
            ],
        ),
    ]