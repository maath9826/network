# Generated by Django 4.0.4 on 2022-04-28 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_alter_post_likes_alter_post_likes_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='follow_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='followers_count',
            field=models.IntegerField(default=0),
        ),
    ]