# Generated by Django 4.0.3 on 2022-03-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='workerID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
            ],
        ),
    ]
