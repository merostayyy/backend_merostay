# Generated by Django 4.1.2 on 2022-10-31 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merostay_api', '0002_remove_hotel_info_room_type_hotel_info_double_room_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel_info',
            name='hotel_info_slug',
        ),
        migrations.AddField(
            model_name='hotel_info',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='hotel_info',
            name='double_room',
            field=models.BooleanField(default=False, verbose_name='Double'),
        ),
        migrations.AlterField(
            model_name='hotel_info',
            name='family_room',
            field=models.BooleanField(default=False, verbose_name='Family'),
        ),
        migrations.AlterField(
            model_name='hotel_info',
            name='luxary_room',
            field=models.BooleanField(default=False, verbose_name='Luxary'),
        ),
        migrations.AlterField(
            model_name='hotel_info',
            name='single_room',
            field=models.BooleanField(default=False, verbose_name='Single'),
        ),
    ]