# Generated by Django 4.0.6 on 2022-08-04 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(default='null', max_length=50, verbose_name='Brand Name')),
                ('name_of_product', models.CharField(max_length=50, verbose_name='Name of Product')),
                ('price', models.FloatField(verbose_name='Product Price')),
                ('theme', models.CharField(default='null', max_length=100, verbose_name='Theme Name')),
                ('product_url1', models.URLField(default='null', verbose_name='Image 1')),
                ('product_url2', models.URLField(default='null', verbose_name='Image 2')),
                ('product_url3', models.URLField(default='null', verbose_name='Image 3')),
                ('product_url4', models.URLField(default='null', verbose_name='Image 4')),
            ],
        ),
        migrations.CreateModel(
            name='DescriptionOfProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='description')),
                ('Product', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='product.products', verbose_name='Description Point')),
            ],
        ),
    ]
