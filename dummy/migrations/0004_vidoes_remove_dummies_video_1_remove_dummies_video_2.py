# Generated by Django 5.1.4 on 2025-01-12 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy', '0003_dummies_video_1_dummies_video_2_alter_dummies_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='vidoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_1', models.FileField(blank=True, upload_to='content/')),
                ('vdeo_2', models.FileField(blank=True, upload_to='content/')),
            ],
        ),
        migrations.RemoveField(
            model_name='dummies',
            name='video_1',
        ),
        migrations.RemoveField(
            model_name='dummies',
            name='video_2',
        ),
    ]
