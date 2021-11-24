# Generated by Django 3.2.9 on 2021-11-12 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_agent_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='image',
            field=models.ImageField(default='img/default-2.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='img/default-1.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='image',
            field=models.ImageField(default='img/default.png', upload_to='images/'),
        ),
    ]