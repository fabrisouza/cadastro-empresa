# Generated by Django 3.2.7 on 2021-10-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_alter_company_useres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='useres',
            field=models.ManyToManyField(related_name='_register_company_useres_+', to='register.Company'),
        ),
    ]
