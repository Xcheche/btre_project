# Generated by Django 5.1.7 on 2025-03-06 14:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("realtors", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="realtor",
            old_name="email",
            new_name="realtor_email",
        ),
    ]
