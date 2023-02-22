# Generated by Django 3.2 on 2023-02-15 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_Client', models.CharField(default='', max_length=50)),
                ('Email', models.EmailField(default='', max_length=50)),
                ('Telephone', models.CharField(blank=True, max_length=8)),
                ('Solde_wallet', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CarItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=15)),
                ('my_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_items', to='clientProfile.clientprofile')),
            ],
        ),
    ]
