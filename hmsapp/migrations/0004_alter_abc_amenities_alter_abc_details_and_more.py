# Generated by Django 5.0.1 on 2024-01-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0003_abc_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abc',
            name='amenities',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='abc',
            name='details',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='abc',
            name='image',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]
