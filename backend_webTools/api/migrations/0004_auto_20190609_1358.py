# Generated by Django 2.2.2 on 2019-06-09 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_interview'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='debtType',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='report',
            name='numDebt',
            field=models.TextField(default='-'),
        ),
    ]
