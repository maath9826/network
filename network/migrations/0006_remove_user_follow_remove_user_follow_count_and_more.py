# Generated by Django 4.0.4 on 2022-04-29 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_alter_post_likes_count_alter_user_follow_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='follow',
        ),
        migrations.RemoveField(
            model_name='user',
            name='follow_count',
        ),
        migrations.RemoveField(
            model_name='user',
            name='followers_count',
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='followings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]