# Generated by Django 2.0 on 2018-02-08 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20180206_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='phone',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customers',
            name='date',
            field=models.FloatField(blank=True, default=1518056421.5320516, null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='added',
            field=models.FloatField(blank=True, default=1518056421.533052, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='added',
            field=models.FloatField(blank=True, default=1518056421.5350559, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='joined',
            field=models.IntegerField(blank=True, default=1518056421.536559),
        ),
    ]
