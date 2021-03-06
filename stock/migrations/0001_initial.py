# Generated by Django 3.1.1 on 2020-09-25 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(help_text='Type Stock Symbol HERE', max_length=4, unique=True)),
                ('update_data', models.DateTimeField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('profit', models.FloatField()),
            ],
        ),
    ]
