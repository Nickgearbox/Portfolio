# Generated by Django 5.0.3 on 2024-03-13 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='content',
            new_name='message',
        ),
    ]
