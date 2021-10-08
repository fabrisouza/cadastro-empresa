# Generated by Django 3.2.7 on 2021-10-07 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin", "0003_logentry_add_action_flag_choices"),
        ("authtoken", "0003_tokenproxy"),
        ("register", "0008_manager"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={},
        ),
        migrations.AlterField(
            model_name="user",
            name="company_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="register.company",
            ),
        ),
        migrations.DeleteModel(
            name="Manager",
        ),
    ]