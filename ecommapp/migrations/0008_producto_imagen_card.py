# Generated by Django 3.1.1 on 2020-09-23 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0007_auto_20200921_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen_card',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
