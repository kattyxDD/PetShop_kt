# Generated by Django 2.1.3 on 2019-10-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.CharField(max_length=20),
        ),
    ]
