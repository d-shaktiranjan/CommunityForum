# Generated by Django 3.2.9 on 2021-12-04 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211205_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='qID',
            field=models.CharField(default=None, max_length=36),
        ),
    ]