# Generated by Django 3.2 on 2023-12-27 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fashionretailsales',
            name='amount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Purchase Amount (USD)'),
        ),
        migrations.AlterField(
            model_name='fashionretailsales',
            name='date_purchased',
            field=models.CharField(max_length=255, verbose_name='Date Purchase'),
        ),
    ]