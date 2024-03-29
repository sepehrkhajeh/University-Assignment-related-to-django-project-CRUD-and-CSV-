# Generated by Django 3.2 on 2023-12-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FashionRetailSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer', models.CharField(max_length=255, verbose_name='Customer Reference ID')),
                ('item', models.CharField(max_length=255, verbose_name='Item Purchased')),
                ('amount', models.PositiveIntegerField(verbose_name='Purchase Amount (USD)')),
                ('date_purchased', models.DateTimeField(verbose_name='Date Purchase')),
                ('Review_Rating', models.CharField(max_length=255, verbose_name='Review Rating')),
                ('Payment_Method', models.CharField(max_length=255, verbose_name='Payment Method')),
            ],
        ),
        migrations.CreateModel(
            name='UploadFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
