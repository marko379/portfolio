# Generated by Django 4.1 on 2023-07-18 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0003_projects_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
