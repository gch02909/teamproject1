# Generated by Django 2.2.2 on 2019-06-29 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jryapp', '0003_auto_20190629_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcroom',
            name='cost',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pcroom',
            name='misc',
            field=models.CharField(default='steam 게임 가능', max_length=50),
            preserve_default=False,
        ),
    ]