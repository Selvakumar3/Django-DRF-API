# Generated by Django 4.1 on 2022-08-16 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars_name', models.CharField(max_length=250)),
                ('cars_colour', models.CharField(max_length=250)),
                ('cars_price', models.IntegerField()),
                ('cars_models', models.CharField(max_length=250)),
            ],
        ),
    ]