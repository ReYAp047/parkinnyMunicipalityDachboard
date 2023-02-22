# Generated by Django 3.2 on 2023-02-15 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_Parking', models.CharField(default='', max_length=50)),
                ('Adresse', models.EmailField(default='', max_length=50)),
                ('Prix_heur', models.FloatField(default=0)),
                ('Date_ouverture', models.DateField(auto_now_add=True)),
                ('Date_fermeture', models.DateField(auto_now_add=True)),
                ('Email', models.EmailField(max_length=30)),
                ('Telephone', models.CharField(blank=True, max_length=8)),
            ],
        ),
    ]