# Generated by Django 4.1.1 on 2022-09-20 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="category",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="tag",
            old_name="tags",
            new_name="name",
        ),
    ]
