# Generated by Django 2.1.1 on 2018-09-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0010_content_content_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
