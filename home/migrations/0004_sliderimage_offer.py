# Generated by Django 4.1.5 on 2023-01-15 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_sliderimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='offer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
