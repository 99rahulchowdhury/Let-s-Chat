# Generated by Django 4.1.3 on 2022-12-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0005_message_imag"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="imag",
        ),
        migrations.AddField(
            model_name="users",
            name="imag",
            field=models.ImageField(default="", upload_to="pics"),
        ),
    ]
