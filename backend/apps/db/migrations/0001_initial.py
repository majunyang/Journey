# Generated by Django 2.0.4 on 2019-06-03 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='MySQLInst',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='db.CommonInfo')),
                ('inst_name', models.CharField(max_length=128, verbose_name='MySQLInst名称')),
                ('inst_host', models.GenericIPAddressField(verbose_name='MySQLInstIP地址')),
                ('inst_port', models.PositiveIntegerField(verbose_name='MySQLInst端口')),
                ('manage_user', models.CharField(max_length=32, verbose_name='MySQLInst管理用户')),
                ('manage_userpwd', models.CharField(max_length=64, verbose_name='MySQLInst管理用户密码')),
                ('read_user', models.CharField(max_length=32, verbose_name='MySQLInst只读用户')),
                ('read_userpwd', models.CharField(max_length=32, verbose_name='MySQLInst只读用户密码')),
                ('role', models.CharField(choices=[('Master', 'Master'), ('Slave', 'Slave')], default='Master', max_length=12, verbose_name='是否启用')),
                ('services', models.CharField(max_length=255, verbose_name='涉及服务')),
                ('version', models.CharField(default=5.7, max_length=32, verbose_name='MYSQL版本')),
                ('is_enabled', models.CharField(choices=[('ENABLED', 'ENABLED'), ('DISABLED', 'DISABLED')], default='ENABLED', max_length=12, verbose_name='是否启用')),
            ],
            options={
                'verbose_name': 'MYSQL实例',
                'verbose_name_plural': 'MYSQL实例',
            },
            bases=('db.commoninfo',),
        ),
    ]
