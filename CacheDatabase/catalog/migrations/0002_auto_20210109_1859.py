# Generated by Django 3.1.4 on 2021-01-09 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoyt',
            name='desc',
            field=models.CharField(max_length=3000),
        ),
    ]