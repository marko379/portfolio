# Generated by Django 4.1 on 2023-07-18 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0002_projects_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='project_images/'),
        ),
    ]
