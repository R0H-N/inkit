# Generated by Django 5.0 on 2024-01-25 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_message_chatmessage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='chatMessage',
            new_name='Message',
        ),
    ]
