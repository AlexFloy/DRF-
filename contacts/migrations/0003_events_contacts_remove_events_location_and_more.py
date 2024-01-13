# Generated by Django 5.0 on 2024-01-12 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='contacts',
            field=models.ManyToManyField(to='contacts.contact'),
        ),
        migrations.RemoveField(
            model_name='events',
            name='location',
        ),
        migrations.AddField(
            model_name='events',
            name='location',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
