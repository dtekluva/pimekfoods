# Generated by Django 2.0 on 2018-02-11 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20180211_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='date',
            field=models.FloatField(blank=True, default=1518308523.4039407, null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='added',
            field=models.FloatField(blank=True, default=1518308523.4039407, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='added',
            field=models.FloatField(blank=True, default=1518308523.4039407, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='joined',
            field=models.IntegerField(blank=True, default=1518308523.4039407),
        ),
    ]
