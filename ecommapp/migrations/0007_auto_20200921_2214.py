# Generated by Django 3.1.1 on 2020-09-22 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0006_auto_20200919_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_pedido',
            name='pedido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommapp.pedido'),
        ),
    ]
