# Generated by Django 2.0.3 on 2018-04-07 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='Firstname',
            new_name='first_name',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='city',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='mobile_no',
            field=models.CharField(max_length=10),
        ),
    ]