# Generated by Django 4.2 on 2023-07-12 12:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0009_alter_brand_image_name_alter_product_image_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=10, unique=True, verbose_name='کد کوپن')),
                ('start_date', models.DateTimeField(verbose_name='تاریخ شروع')),
                ('end_date', models.DateTimeField(verbose_name='تاریخ پایان')),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='درصد تخفیف')),
                ('is_active', models.BooleanField(default=False, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'کوپن تخفیف',
                'verbose_name_plural': 'کوپنها',
            },
        ),
        migrations.CreateModel(
            name='DiscountBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_title', models.CharField(max_length=100, verbose_name='عنوان سبد تخفیف')),
                ('start_date', models.DateTimeField(verbose_name='تاریخ شروع')),
                ('end_date', models.DateTimeField(verbose_name='تاریخ پایان')),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='درصد تخفیف')),
                ('is_active', models.BooleanField(default=False, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'سبد تخفیف',
                'verbose_name_plural': 'سبد های تخفیف',
            },
        ),
        migrations.CreateModel(
            name='DiscountBasketDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount_basket_details1', to='discounts.discountbasket', verbose_name='سبد تخفیف')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount_basket_details2', to='products.product', verbose_name='کالا')),
            ],
            options={
                'verbose_name': 'جزییات سبد تخفیف',
            },
        ),
    ]
