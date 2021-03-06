# Generated by Django 3.0.4 on 2020-03-15 21:52

import cloud_project.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(storage=cloud_project.storage_backends.StaticStorage(), upload_to='')),
            ],
        ),
    ]
