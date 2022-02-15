# Generated by Django 1.11.26 on 2020-01-27 22:03
from django.db import migrations, models

STREAM_POST_POLICY_EVERYONE = 1


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0262_mutedtopic_date_muted"),
    ]

    operations = [
        migrations.AddField(
            model_name="stream",
            name="stream_post_policy",
            field=models.PositiveSmallIntegerField(default=STREAM_POST_POLICY_EVERYONE),
        ),
    ]
