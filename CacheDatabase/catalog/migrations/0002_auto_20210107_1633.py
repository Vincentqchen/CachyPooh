# Generated by Django 3.1.4 on 2021-01-07 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('die', models.CharField(max_length=600)),
            ],
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.DeleteModel(
            name='YoutubeCache',
        ),
    ]
