# Generated by Django 4.0.6 on 2022-07-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societe', '0002_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='status',
            field=models.CharField(choices=[('En attente', 'En attente'), ('Résolu', 'Résolu')], max_length=200, null=True),
        ),
    ]