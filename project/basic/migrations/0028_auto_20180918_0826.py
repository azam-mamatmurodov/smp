# Generated by Django 2.1.1 on 2018-09-18 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0027_youtubevideoalbum_video_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubevideoalbum',
            name='video_type',
            field=models.CharField(choices=[('personal', 'Personal videos'), ('audio', 'Audio materials'), ('video', 'Video materials'), ('cognitive', 'Cognitive materials')], default='personal', max_length=60),
        ),
    ]
