# Generated by Django 3.1.1 on 2020-09-23 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0005_auto_20200916_0509'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen_card',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FileField(upload_to=''),
        ),
    ]