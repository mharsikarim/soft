# Generated by Django 4.0.6 on 2022-07-18 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societe', '0010_remove_message_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
