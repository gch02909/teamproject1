# Generated by Django 2.2.2 on 2019-06-29 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PCRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('spec', models.TextField()),
                ('maxPeopleNumber', models.IntegerField()),
                ('peopleNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PeopleNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcroom', models.CharField(max_length=50)),
                ('accupied', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representName', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=20)),
                ('representContact', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('sponsor', models.CharField(default='없음', max_length=20)),
                ('pcroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jryapp.PCRoom')),
                ('peopleNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jryapp.PeopleNumber')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
