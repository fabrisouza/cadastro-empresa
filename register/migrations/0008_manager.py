# Generated by Django 3.2.7 on 2021-10-06 01:54

from django.db import migrations, models
import django.db.models.deletion
import register.managers


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_rename_name_company_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='register.user')),
            ],
            options={
                'verbose_name_plural': 'Manager',
            },
            bases=('register.user',),
            managers=[
                ('objects', register.managers.UserManager()),
            ],
        ),
    ]
