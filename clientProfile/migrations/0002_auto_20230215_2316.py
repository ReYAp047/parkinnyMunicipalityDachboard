# Generated by Django 3.2 on 2023-02-15 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientProfile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarMatricule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matricule', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='CarItem',
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='CarMatricule',
            field=models.ManyToManyField(blank=True, to='clientProfile.CarMatricule'),
        ),
    ]
