# Generated by Django 2.1.5 on 2019-02-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(),
        ),
    ]
