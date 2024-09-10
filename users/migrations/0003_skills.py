# Generated by Django 5.0.6 on 2024-08-26 10:06

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profiles_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('e_skill', models.TextField(blank=True, max_length=500, null=True)),
                ('ult_skill', models.TextField(blank=True, max_length=500, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profiles')),
            ],
        ),
    ]
