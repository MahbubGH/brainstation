# Generated by Django 2.0.8 on 2018-09-19 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0002_auto_20180918_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=13)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]