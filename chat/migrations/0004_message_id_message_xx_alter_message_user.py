# Generated by Django 4.1.3 on 2022-12-20 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0003_remove_message_id_alter_message_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=0,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="message",
            name="xx",
            field=models.CharField(default="0", max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="message",
            name="user",
            field=models.CharField(max_length=1000),
        ),
    ]