# Generated by Django 3.2.7 on 2021-10-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20211001_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]