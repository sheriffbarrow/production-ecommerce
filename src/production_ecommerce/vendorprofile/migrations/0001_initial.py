# Generated by Django 2.1.2 on 2020-01-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('emailId', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('contactNo', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='media/')),
            ],
        ),
    ]
