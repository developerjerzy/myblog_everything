# Generated by Django 3.2.9 on 2021-12-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body_double',
            field=models.TextField(),
        ),
    ]
