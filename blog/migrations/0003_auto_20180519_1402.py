# Generated by Django 2.0.2 on 2018-05-19 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='url',
            field=models.URLField(max_length=400),
        ),
    ]
