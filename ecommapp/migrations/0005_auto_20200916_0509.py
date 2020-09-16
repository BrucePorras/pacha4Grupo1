# Generated by Django 3.1 on 2020-09-16 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0004_auto_20200916_0505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cupon',
        ),
        migrations.AddField(
            model_name='producto',
            name='descuento',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommapp.cupon'),
        ),
    ]