# Generated by Django 2.2.4 on 2020-05-08 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='outreach',
            name='location',
            field=models.CharField(default='No where', max_length=200),
        ),
    ]
