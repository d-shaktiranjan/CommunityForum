# Generated by Django 4.0.3 on 2022-04-10 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_answers_bystudent_quentions_bystudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='quentions',
            name='correntAnswer',
            field=models.CharField(blank=True, max_length=36),
        ),
        migrations.AddField(
            model_name='quentions',
            name='isFixed',
            field=models.BooleanField(default=False),
        ),
    ]