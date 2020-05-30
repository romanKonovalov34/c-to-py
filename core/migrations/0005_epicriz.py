# Generated by Django 3.0.6 on 2020-05-30 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200530_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epicriz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invalid', models.BooleanField(default=False)),
                ('lechenie', models.TextField()),
                ('date_gospit', models.DateField()),
                ('date_vipisky', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.User')),
            ],
            options={
                'verbose_name': 'эпикриз',
                'verbose_name_plural': 'эпикризы',
            },
        ),
    ]
