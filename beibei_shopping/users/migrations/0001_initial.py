# Generated by Django 2.1.1 on 2018-10-17 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=255, unique=True, verbose_name='用户昵称')),
                ('age', models.IntegerField(default=18, verbose_name='用户年龄')),
                ('gender', models.CharField(default='男', max_length=10, verbose_name='用户性别')),
                ('header', models.ImageField(default='static/images/headers/beibei.png', upload_to='static/images/headers', verbose_name='用户头像')),
                ('phone', models.IntegerField(default=123456, max_length=50, verbose_name='用户手机号码')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
