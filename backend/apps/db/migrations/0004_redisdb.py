# Generated by Django 2.0.4 on 2019-03-11 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_auto_20190121_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedisDB',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=128, verbose_name='Redis数据库名')),
                ('host', models.GenericIPAddressField(blank=True, null=True, verbose_name='Redis IP地址')),
                ('port', models.PositiveIntegerField(blank=True, default=3306, null=True, verbose_name='Redis端口')),
                ('password', models.CharField(max_length=64, verbose_name='Redis密码')),
                ('version', models.CharField(default=5.7, max_length=32, verbose_name='Redis版本')),
                ('is_enabled', models.PositiveSmallIntegerField(choices=[(0, '禁用'), (1, '启用')], verbose_name='是否启用')),
            ],
            options={
                'verbose_name': 'Redis数据库',
                'verbose_name_plural': 'Redis数据库',
                'db_table': 'redis_db',
            },
        ),
    ]
