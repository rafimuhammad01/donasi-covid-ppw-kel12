# Generated by Django 3.1.2 on 2020-11-13 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pertanyaan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='detail',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]