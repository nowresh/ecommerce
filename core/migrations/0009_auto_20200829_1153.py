# Generated by Django 2.2.14 on 2020-08-29 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200829_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(blank=True, choices=[('S', 'sale'), ('N', 'new'), ('P', 'promotion')], max_length=1, null=True),
        ),
    ]
