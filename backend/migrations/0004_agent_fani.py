# Generated by Django 3.2.9 on 2021-11-11 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_agent_lead'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='fani',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]