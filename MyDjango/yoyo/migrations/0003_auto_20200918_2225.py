# Generated by Django 2.0.3 on 2020-09-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoyo', '0002_chengji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peroninfo',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
