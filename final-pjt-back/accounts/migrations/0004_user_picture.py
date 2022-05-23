# Generated by Django 3.2.12 on 2022-05-23 01:09

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_watch_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='../static/accounts/default_profile.jpg', upload_to='profile/'),
        ),
    ]
