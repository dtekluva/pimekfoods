# Generated by Django 2.0 on 2018-02-01 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20180201_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='added',
            field=models.FloatField(blank=True, default=1517447637.468261, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='date',
            field=models.FloatField(blank=True, default=1517447637.4672601, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='added',
            field=models.FloatField(blank=True, default=1517447637.470263, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='joined',
            field=models.IntegerField(blank=True, default=1517447637.4717667),
        ),
    ]
