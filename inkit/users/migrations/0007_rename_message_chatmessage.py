# Generated by Django 5.0 on 2024-01-25 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_message_recepient'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='chatMessage',
        ),
    ]