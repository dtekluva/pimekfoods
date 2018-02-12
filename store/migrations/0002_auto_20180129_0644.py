# Generated by Django 2.0 on 2018-01-29 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('price', models.IntegerField(default=0)),
                ('details', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('comments', models.IntegerField(default=0)),
                ('pub_date', models.DateField(auto_now=True)),
                ('added', models.FloatField(blank=True, default=1517204663.7870736, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='product-imgs/')),
                ('posted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='profile-imgs/')),
                ('joined', models.IntegerField(blank=True, default=1517204663.7880745)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Accounts',
            },
        ),
        migrations.AlterField(
            model_name='customers',
            name='date',
            field=models.FloatField(blank=True, default=1517204663.7845685, null=True),
        ),
    ]
