# Generated by Django 3.2.7 on 2021-10-01 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_user_company_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.company'),
        ),
    ]
