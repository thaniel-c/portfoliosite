# Generated by Django 3.0.5 on 2020-04-29 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='githubLink',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='otherLink',
            field=models.TextField(null=True),
        ),
    ]
