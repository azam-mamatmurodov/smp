# Generated by Django 2.1.1 on 2018-09-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0016_auto_20180916_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('file', models.FileField(upload_to='library/files/')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='', verbose_name='library/images/')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
