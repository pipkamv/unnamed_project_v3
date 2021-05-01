# Generated by Django 3.1.5 on 2021-05-01 07:55

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
            name='AddProductToExcelFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tnved', models.CharField(default='', max_length=64)),
                ('full_product_name', models.CharField(default='', max_length=128)),
                ('trademark', models.CharField(default='', max_length=64)),
                ('article_type', models.CharField(default='', max_length=64)),
                ('article_value', models.CharField(default='', max_length=64)),
                ('product_type', models.CharField(default='', max_length=64)),
                ('color', models.CharField(default='', max_length=64)),
                ('target_gender', models.CharField(default='', max_length=64)),
                ('clothing_type', models.CharField(default=0, max_length=64)),
                ('clothing_value', models.CharField(default=0, max_length=64)),
                ('composition', models.CharField(default='', max_length=64)),
                ('standard_no', models.CharField(default='', max_length=64)),
                ('status', models.CharField(default='', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel_file', models.FileField(blank=True, null=True, upload_to='excel_files/')),
                ('file_name', models.CharField(default='', max_length=64)),
                ('is_order', models.BooleanField(default=False)),
                ('date_send', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExcelFileTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel_file', models.FileField(upload_to='excel_file_templates')),
                ('file_name', models.CharField(default='', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tnved', models.CharField(default='', max_length=64)),
                ('full_product_name', models.CharField(default='', max_length=128)),
                ('trademark', models.CharField(default='', max_length=64)),
                ('article_type', models.CharField(default='', max_length=64)),
                ('article_value', models.CharField(default='', max_length=64)),
                ('product_type', models.CharField(default='', max_length=64)),
                ('color', models.CharField(default='', max_length=64)),
                ('target_gender', models.CharField(default='', max_length=64)),
                ('clothing_type', models.CharField(default='', max_length=64)),
                ('clothing_value', models.CharField(default='', max_length=64)),
                ('composition', models.CharField(default='', max_length=64)),
                ('standard_no', models.CharField(default='', max_length=64)),
                ('status', models.CharField(default='', max_length=64)),
                ('result_treatment_data', models.CharField(default='', max_length=64)),
                ('excel_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.excelfile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
