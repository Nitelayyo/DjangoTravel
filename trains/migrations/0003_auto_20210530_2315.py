# Generated by Django 3.2.3 on 2021-05-30 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_alter_city_options'),
        ('trains', '0002_traintest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='from_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city_set', to='cities.city', verbose_name='Откуда'),
        ),
        migrations.AlterField(
            model_name='train',
            name='to_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city_set', to='cities.city', verbose_name='Куда'),
        ),
        migrations.AlterField(
            model_name='traintest',
            name='from_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_from_city_set', to='cities.city', verbose_name='Откуда'),
        ),
    ]
