# Generated by Django 2.0 on 2018-02-06 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20180201_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='date',
            field=models.FloatField(blank=True, default=1517889984.6005404, null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='added',
            field=models.FloatField(blank=True, default=1517889984.6020434, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='added',
            field=models.FloatField(blank=True, default=1517889984.603545, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='details',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='joined',
            field=models.IntegerField(blank=True, default=1517889984.6055477),
        ),
    ]
