# Generated by Django 5.1.3 on 2024-11-19 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredictionInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temp1', models.FloatField()),
                ('Press1', models.FloatField()),
                ('Temp2', models.FloatField()),
                ('Press2', models.FloatField()),
                ('Status', models.FloatField()),
            ],
        ),
    ]
