# Generated by Django 4.1.5 on 2023-01-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category_imgs/'),
        ),
    ]
