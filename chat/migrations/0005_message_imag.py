# Generated by Django 4.1.3 on 2022-12-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0004_message_id_message_xx_alter_message_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="imag",
            field=models.ImageField(default="", upload_to="pics"),
        ),
    ]