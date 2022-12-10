# Generated by Django 4.1.2 on 2022-11-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookM',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('bid', models.CharField(max_length=100, unique=True)),
                ('bname', models.CharField(max_length=100)),
                ('publication', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('bcat', models.CharField(max_length=100)),
            ],
        ),
    ]