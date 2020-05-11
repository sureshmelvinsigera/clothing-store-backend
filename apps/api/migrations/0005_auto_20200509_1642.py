# Generated by Django 3.0.6 on 2020-05-09 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200509_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='description',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='pictureUrl',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='price',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='api.CartItem'),
        ),
    ]
