# Generated by Django 2.0.4 on 2020-03-11 17:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_auto_20200309_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='api',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='perms',
        ),
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('4fb3e3c4-0e4f-4b2c-98b3-c78c829d38e3'), verbose_name='用户jwt加密秘钥'),
        ),
    ]