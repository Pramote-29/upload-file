# Generated by Django 5.1.4 on 2025-01-11 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=models.BinaryField(verbose_name='ไฟล์รูปภาพ'),
        ),
    ]