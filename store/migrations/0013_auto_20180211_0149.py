# Generated by Django 2.0 on 2018-02-11 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20180211_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='date',
            field=models.FloatField(blank=True, default=1518310169.1880834, null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='added',
            field=models.FloatField(blank=True, default=1518310169.190413, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='hits',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='added',
            field=models.FloatField(blank=True, default=1518310169.1924138, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='joined',
            field=models.IntegerField(blank=True, default=1518310169.194419),
        ),
    ]
