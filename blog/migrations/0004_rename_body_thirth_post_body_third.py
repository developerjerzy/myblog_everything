# Generated by Django 3.2.9 on 2021-12-28 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211228_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body_thirth',
            new_name='body_third',
        ),
    ]