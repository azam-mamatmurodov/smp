# Generated by Django 2.1.1 on 2018-09-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0028_auto_20180918_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='Саморазвитие и Самопознание', max_length=254)),
                ('site_logo', models.ImageField(default='logo.webp', upload_to='site/')),
            ],
        ),
    ]
