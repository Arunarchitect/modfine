# Generated by Django 4.2.2 on 2023-06-17 06:20

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='notes',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
    ]
