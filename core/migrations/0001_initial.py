# Generated by Django 3.0.6 on 2020-05-27 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_card', models.IntegerField(max_length=50, verbose_name='Номер карты')),
                ('FIO', models.CharField(max_length=100, verbose_name='ФИО')),
                ('date_birth', models.CharField(max_length=100, verbose_name='Дата рождения')),
                ('sex', models.CharField(max_length=50, verbose_name='Пол')),
                ('nationality', models.CharField(max_length=50, verbose_name='Национальность')),
                ('education', models.CharField(max_length=100, verbose_name='Образование')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('job', models.CharField(max_length=100, verbose_name='Место работы')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'пациента',
                'verbose_name_plural': 'пациенты',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200, verbose_name='ФИО')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
                ('isAdmin', models.BooleanField(verbose_name='Я администратор')),
            ],
            options={
                'verbose_name': 'пользователя',
                'verbose_name_plural': 'пользователи',
            },
        ),
    ]