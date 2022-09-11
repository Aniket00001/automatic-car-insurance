# Generated by Django 3.0.3 on 2020-02-22 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
                ('document1', models.FileField(upload_to='documents/')),
                ('document2', models.FileField(upload_to='documents/')),
                ('document3', models.FileField(upload_to='documents/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
