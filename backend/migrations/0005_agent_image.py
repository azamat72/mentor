# Generated by Django 3.2.9 on 2021-11-12 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_agent_fani'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='image',
            field=models.ImageField(default='images/defoult.png', upload_to='images/'),
        ),
    ]