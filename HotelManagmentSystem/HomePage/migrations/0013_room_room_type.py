# Generated by Django 4.2.7 on 2023-12-10 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0012_remove_room_check_in_date_remove_room_check_out_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(default='Standard', on_delete=django.db.models.deletion.CASCADE, to='HomePage.roomtype'),
            preserve_default=False,
        ),
    ]
