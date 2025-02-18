# Generated by Django 5.1.6 on 2025-02-18 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(help_text='Enter your OpenWeatherMap API key here', max_length=255)),
            ],
            options={
                'verbose_name': 'Weather Configuration',
                'verbose_name_plural': 'Weather Configurations',
            },
        ),
    ]
