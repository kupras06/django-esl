# Generated by Django 3.1.4 on 2021-01-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esl', '0005_auto_20210104_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='date',
            field=models.DateField(),
        ),
    ]
