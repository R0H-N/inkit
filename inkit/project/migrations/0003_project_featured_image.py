# Generated by Django 5.0 on 2024-01-03 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
