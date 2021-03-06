# Generated by Django 3.0.6 on 2020-05-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200509_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Dresses', 'Dresses'), ('Tops', 'Tops'), ('Bottoms', 'Bottoms'), ('Necklaces', 'Necklaces'), ('Bracelets', 'Bracelets'), ('Earrings', 'Earrings'), ('Sale', 'Sale')], max_length=100),
        ),
    ]
