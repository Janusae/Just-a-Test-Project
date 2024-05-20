# Generated by Django 5.0.4 on 2024-05-20 09:52

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_alter_user_plus_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_plus',
            name='avatar',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[300, 300], upload_to='avatars'),
        ),
    ]