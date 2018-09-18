# Generated by Django 2.1.1 on 2018-09-15 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0014_youtubevideotranslation_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubevideo',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='videos', to='basic.YouTubeVideoAlbum'),
        ),
    ]
