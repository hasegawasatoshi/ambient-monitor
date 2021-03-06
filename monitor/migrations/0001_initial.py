# Generated by Django 3.2.5 on 2021-07-28 07:55

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='numeric, alphabet or hylien', regex='^[0-9a-zA-Z-]+$')], verbose_name='S/N')),
                ('label', models.CharField(blank=True, max_length=128, verbose_name='Label')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
