# Generated by Django 5.1.4 on 2024-12-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
    ]