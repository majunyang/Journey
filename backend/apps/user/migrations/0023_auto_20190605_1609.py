# Generated by Django 2.0.4 on 2019-06-05 08:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_auto_20190605_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('414c4975-0839-4a88-96b1-43641c0f7381'), verbose_name='用户jwt加密秘钥'),
        ),
    ]
