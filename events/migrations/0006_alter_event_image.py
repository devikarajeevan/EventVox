# Generated by Django 4.2.7 on 2023-11-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0005_event_image_alter_event_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="events_pics"),
        ),
    ]
