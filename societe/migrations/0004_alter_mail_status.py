# Generated by Django 4.0.6 on 2022-07-13 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societe', '0003_mail_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
