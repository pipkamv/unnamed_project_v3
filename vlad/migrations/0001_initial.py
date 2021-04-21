# Generated by Django 3.1.5 on 2021-04-21 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VladModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Было добавлено')),
                ('from_whom', models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='От кого')),
                ('user_exel_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.excelfile', verbose_name='Файл пользователя')),
            ],
            options={
                'verbose_name': 'заказ посетителей',
                'verbose_name_plural': 'заказы посетителей',
            },
        ),
    ]
