# Generated by Django 2.2.7 on 2019-11-13 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
