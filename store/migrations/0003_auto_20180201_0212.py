# Generated by Django 2.0 on 2018-02-01 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20180129_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='isread',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customers',
            name='date',
            field=models.FloatField(blank=True, default=1517447523.2794926, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='added',
            field=models.FloatField(blank=True, default=1517447523.2794926, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='joined',
            field=models.IntegerField(blank=True, default=1517447523.2794926),
        ),
    ]