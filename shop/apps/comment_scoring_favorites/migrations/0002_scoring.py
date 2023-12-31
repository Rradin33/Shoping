# Generated by Django 4.2 on 2023-08-18 10:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_brand_image_name_alter_product_image_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment_scoring_favorites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='scoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registerdate', models.DateField(auto_now_add=True, verbose_name='تاریخ درج')),
                ('score', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='امتیاز')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scoring_product', to='products.product', verbose_name='کالا')),
                ('scoring_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scoring_user1', to=settings.AUTH_USER_MODEL, verbose_name='امتیاز دهنده')),
            ],
            options={
                'verbose_name': 'امتیاز',
                'verbose_name_plural': 'امتیازات',
            },
        ),
    ]
