# Generated by Django 4.2 on 2023-07-03 18:26

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image_name',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to, verbose_name='تصویر  پروفایل'),
        ),
    ]
