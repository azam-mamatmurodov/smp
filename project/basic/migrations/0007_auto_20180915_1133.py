# Generated by Django 2.1.1 on 2018-09-15 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0006_auto_20180915_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='level',
            new_name='mptt_level',
        ),
    ]
