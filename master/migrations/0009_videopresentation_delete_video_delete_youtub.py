# Generated by Django 4.0.2 on 2022-02-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0008_youtub'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPresentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
                ('video_url', models.URLField()),
                ('desc', models.TextField()),
                ('youtub_chanel_url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.DeleteModel(
            name='Youtub',
        ),
    ]
