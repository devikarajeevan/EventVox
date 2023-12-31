# Generated by Django 4.2.7 on 2023-11-12 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0004_alter_event_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="profile_pics"),
        ),
        migrations.AlterField(
            model_name="event", name="date", field=models.DateField(),
        ),
    ]
