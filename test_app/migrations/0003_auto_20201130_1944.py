# Generated by Django 3.1.3 on 2020-11-30 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_app", "0002_auto_20201130_1156"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="upvotes",
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name="Upvote",
        ),
    ]
